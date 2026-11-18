"""Small, honest statistics helpers.

For young readers
-----------------
If you flip a coin many times, you will sometimes get five heads in a row
just by luck. Scientists must check that an exciting signal is not just luck.
The more places you look, the more likely luck fools you.

For experts
-----------
* Gaussian sigma <-> p-value conversions (one- or two-sided).
* Look-elsewhere (trials) correction for N independent trials:
  p_global = 1 - (1 - p_local)^N, computed stably.
* Gumbel (extreme-value type I) CDF and return period
  T(x) = 1 / (1 - F(x)). The return period answers "how many blocks (years,
  sectors, nights) until a maximum this large recurs?" It is *not* a detection
  significance by itself.
"""

from __future__ import annotations

import math

import numpy as np
from scipy.stats import norm

__all__ = ["sigma_to_p", "p_to_sigma", "trials_corrected_p", "gumbel_cdf", "gumbel_return_period",
           "fit_gumbel_moments"]


def sigma_to_p(sigma: float, two_sided: bool = False) -> float:
    p = float(norm.sf(sigma))
    return 2.0 * p if two_sided else p


def p_to_sigma(p: float, two_sided: bool = False) -> float:
    if not 0.0 < p <= 1.0:
        raise ValueError("p must be in (0, 1]")
    return float(norm.isf(p / 2.0 if two_sided else p))


def trials_corrected_p(p_local: float, n_trials: float) -> float:
    if not 0.0 <= p_local <= 1.0:
        raise ValueError("p_local must be in [0, 1]")
    if p_local == 1.0:
        return 1.0
    return float(-math.expm1(n_trials * math.log1p(-p_local)))


def gumbel_cdf(x, mu: float, beta: float):
    z = (np.asarray(x, dtype=np.float64) - mu) / beta
    return np.exp(-np.exp(-z))


def gumbel_return_period(x, mu: float, beta: float):
    return 1.0 / (1.0 - gumbel_cdf(x, mu, beta))


def fit_gumbel_moments(block_maxima) -> tuple[float, float]:
    """Method-of-moments Gumbel fit: beta = s sqrt(6)/pi, mu = mean - gamma beta."""
    x = np.asarray(block_maxima, dtype=np.float64)
    beta = float(np.std(x, ddof=1) * math.sqrt(6.0) / math.pi)
    mu = float(np.mean(x) - 0.5772156649015329 * beta)
    return mu, beta
