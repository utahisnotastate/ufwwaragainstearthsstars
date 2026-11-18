# Guide for Physicists

> **In one sentence:** Every disclosure in this project reduces to standard physics — two-body and restricted three-body dynamics, secular perturbation theory, gravitational lensing, radiative transfer and statistics — and this page collects the core results, the pitfalls, and where a physicist's skills help most.

## For young readers

This page is for grown-up scientists, so it has lots of math. The big idea is simple: all the ideas in this project use the same rules of physics that scientists have tested for hundreds of years — like gravity pulling things together and light traveling at a fixed speed. If you want the kid version, try the [lessons](../lessons/README.md)!

## Scope and stance

- We use **Newtonian gravity** (with general-relativistic corrections where they matter), **classical electrodynamics** and **standard statistical inference**.
- Ideas from the original brainstorming notes that required non-standard physics (for example, "scalar" electromagnetic modes, push/shadowing theories of gravity, or faster-than-light position sensing) were removed. The [editorial notes](../about/editorial-notes.md) list them and give the reasons. In brief: Le Sage–type shadowing models predict drag, heating and gravitational shielding that are not observed; and the propagation speed of gravity equals *c* to about one part in 10¹⁵ (GW170817). See Will (2014) for the broader experimental status of gravitation.

## 1. Unbound two-body motion (D14, D15)

With μ = *GM*☉, specific energy and angular momentum:

$$
\varepsilon = \frac{v^2}{2} - \frac{\mu}{r}, \qquad \mathbf{h} = \mathbf{r}\times\mathbf{v}, \qquad e = \sqrt{1 + \frac{2\varepsilon h^2}{\mu^2}}.
$$

For ε > 0: *a* = −μ/(2ε) < 0, *e* > 1, *v*∞ = √(2ε), and *q* = *a*(1 − *e*), so *v*∞² = μ(*e* − 1)/*q*. The asymptotes satisfy cos θ∞ = −1/*e*, and the total deflection is δ = 2 arcsin(1/*e*).

The **incoming asymptote** (the "radiant", the direction the body came from) is not the direction of the current velocity. It follows from the eccentricity vector **e** = (**v** × **h**)/μ − **r**/*r* and the asymptotic true anomaly; the `fdastro.kepler` module computes it. Using the instantaneous velocity direction near perihelion can be wrong by tens of degrees.

**Propagation.** For all conic types use universal variables (Stumpff functions *c*₂, *c*₃) with Lagrange *f* and *g* coefficients. Constant-acceleration Taylor steps over days near the Sun are not adequate for orbit fitting.

**Observation model.** A geocentric (or topocentric) astrometric position requires: the observer's barycentric/heliocentric position at the observation time; the **light-time** solution (the object's position at *t* − ρ/*c*); and, for precise work, aberration and the observer's offset from the geocenter. For an object 0.1 au away, ignoring topocentric parallax can cause errors up to roughly an arcminute.

## 2. Short-arc orbit determination and the bound-orbit test (D14)

Angles-only data over a short arc constrain the attributable (α, δ, α̇, δ̇) well but leave range and range-rate (ρ, ρ̇) poorly constrained. The set of (ρ, ρ̇) consistent with the data — the **admissible region** (Milani et al. 2004) — often spans both bound and unbound orbits. Eccentricity is strongly nonlinear in (ρ, ρ̇), so Gaussian covariance estimates for *e* are unreliable for short arcs; statistical ranging (Virtanen et al. 2001) or MCMC is preferred.

**A fair test of "is it unbound?"** Fit the unconstrained six-parameter model, then refit with ε ≤ 0. The statistic Δχ² = χ²_bound − χ²_free tests a null on the boundary of parameter space; asymptotically it follows a 50:50 mixture of χ²₀ and χ²₁ (Chernoff 1954; Self & Liang 1987). Because short-arc problems are far from asymptotic, **calibrate the false-alarm rate by simulation** with realistic noise, cadence and outliers. Report: arc length, number of observations, RMS, Δχ², the simulated false-alarm rate, and the range of *e* over the admissible region.

**Classical pitfalls:** fitting a model with more freedom than the data constrain; declaring a classification ("confirmed interstellar") from a single short-arc best fit; ignoring UTC/TT offsets (about 69 s in 2026); ignoring outliers and false linkages between tracklets.

## 3. The restricted three-body problem and the Tisserand parameter (D06, D11, D15)

In the circular restricted three-body problem (CR3BP), in units where the primaries' separation, total mass and angular velocity are 1, the Jacobi integral is

$$
C_J = 2U(x,y,z) - (\dot x^2 + \dot y^2 + \dot z^2), \qquad U = \tfrac12(x^2+y^2) + \frac{1-\mu}{r_1} + \frac{\mu}{r_2}.
$$

Zero-velocity surfaces *C*_J = 2*U* bound the allowed regions. The triangular points L4/L5 are linearly stable when μ < μ_Routh ≈ 0.0385 (mass ratio ≳ 24.96). Earth–Moon L4/L5 satisfy this, but solar perturbations make the real four-body problem far less benign.

For a small body far from the planet, expressing *C*_J in heliocentric elements gives the **Tisserand parameter** with respect to a planet with semi-major axis *a*_P:

$$
T_P = \frac{a_P}{a} + 2\cos i\,\sqrt{\frac{a}{a_P}(1-e^2)}.
$$

*T*_J is approximately conserved through encounters with Jupiter (assuming a circular planetary orbit and neglecting other perturbers). Asteroids typically have *T*_J > 3, Jupiter-family comets 2 < *T*_J < 3, and Halley-type/long-period comets *T*_J < 2. Retrograde orbits (cos *i* < 0) can give *T*_J < 0. A low or negative *T*_J is a **dynamical clue**, not proof, of an origin outside the planetary region. Example: (514107) Kaʻepaokaʻawela with *a* ≈ 5.14 au, *e* ≈ 0.38, *i* ≈ 163° has *T*_J ≈ −0.7.

## 4. Secular dynamics and tilted orbits (D02, D13)

**Stellar oblateness.** To lowest order, a star's quadrupole *J*₂ drives nodal precession of a planet's orbit about the stellar spin axis:

$$
\dot\Omega_\star \simeq -\tfrac32\, n\, J_2 \left(\frac{R_\star}{a}\right)^2 \cos\psi .
$$

**Planet–planet secular coupling (Laplace–Lagrange).** For an inner planet 1 perturbed by an outer planet 2, with α = *a*₁/*a*₂,

$$
\dot\Omega_{1} \sim -\tfrac14\, n_1\, \frac{m_2}{M_\star}\, \alpha^2\, b^{(1)}_{3/2}(\alpha), \qquad
b^{(j)}_{s}(\alpha) = \frac{1}{\pi}\int_0^{2\pi}\frac{\cos j\psi\,d\psi}{(1-2\alpha\cos\psi+\alpha^2)^{s}},
$$

with *b*⁽¹⁾₃/₂(α) ≈ 3α for α ≪ 1. Setting the two precession rates comparable gives a locus in (*m*₂, *a*₂) where a secular resonance could excite or maintain a spin–orbit misalignment, approximately (*m*₂/*M*★)(*a*₁/*a*₂)³ ≈ 2*J*₂(*R*★/*a*₁)² cos ψ. This is a **targeting tool** for radial-velocity and astrometric follow-up, not a detection. Many other mechanisms produce misalignment (primordial disk tilts, Kozai–Lidov cycles, planet–planet scattering, resonance crossing during disk dispersal). See Murray & Dermott (1999) for the theory.

**Vanishing transits.** For a circular orbit the impact parameter is *b* = (*a*/*R*★) cos *i*; transits cease when *b* ≳ 1 + *R*ₚ/*R*★. Nodal precession makes *i* (relative to the line of sight) drift, so depth and duration evolve monotonically before transits stop — as observed for TOI-2535 b (Yee et al. 2026).

## 5. Gravitational microlensing (D07)

For a point lens,

$$
\theta_E = \sqrt{\frac{4GM}{c^2}\,\frac{D_{LS}}{D_L D_S}},\qquad t_E = \frac{\theta_E}{\mu_{\rm rel}},\qquad
A(u) = \frac{u^2+2}{u\sqrt{u^2+4}},\qquad u(t)=\sqrt{u_0^2 + \left(\frac{t-t_0}{t_E}\right)^2}.
$$

*t*_E ∝ √*M*, so for typical bulge geometries Earth-mass lenses give events lasting about an hour or less. For such short events, **finite-source effects** (ρ★ = θ★/θ_E ≳ *u*₀) dominate the light-curve shape and are what allow θ_E — and thus a mass–distance relation — to be measured. Lensing is achromatic to first order; strong color changes indicate stellar variability or blending.

## 6. Astrometry: parallax and proper motion (D04)

The standard five-parameter model for small offsets is

$$
\Delta\alpha^* = \Delta\alpha_0^* + \mu_{\alpha^*}(t - t_0) + \varpi\, P_\alpha(t), \qquad
\Delta\delta = \Delta\delta_0 + \mu_\delta (t - t_0) + \varpi\, P_\delta(t),
$$

with parallax factors *P*_α = *X* sin α − *Y* cos α and *P*_δ = *X* cos α sin δ + *Y* sin α sin δ − *Z* cos δ, where (*X*, *Y*, *Z*) is the observer's barycentric position in au (equatorial frame). Transverse speed is *v*_t = 4.74 μ *d* km s⁻¹ (μ in ″/yr, *d* in pc). Linking detections of nearby objects across years requires search radii large enough to include parallax plus proper motion; this is a **combinatorial** problem, and controlling false linkages is the hard part.

## 7. Statistics: look-elsewhere effects and extreme values

- **Trials factor.** A local *p*-value *p*_loc from the best of *N*_eff effectively independent trials corresponds to a global *p* ≈ 1 − (1 − *p*_loc)^*N*_eff. Archive-wide searches can have *N*_eff in the millions; a "4σ local" signal is then expected by chance.
- **Extreme-value statistics.** The maximum of many independent noise values follows a Gumbel (or other generalized extreme-value) distribution. The return period *T*(*x*) = 1/[1 − *F*(*x*)] is the mean number of trials per exceedance of *x*. It is a statement about noise, not a "significance of a discovery", unless *F* is the correctly calibrated null distribution of the search statistic.
- **Injection–recovery** with realistic, non-Gaussian, correlated noise is the gold standard for measuring completeness and false-alarm rates. Red noise in light curves and astrometry is common.
- **Quadrature tests (D12).** A 90° phase relation between TTV and TDV can arise by chance in short, noisy, aliased series. Assess significance by permutation or by fitting the full planet–moon model and comparing evidence.

## 8. Where physicists can help most

1. **Numerical dynamics:** fast, validated propagators; hyperbolic linking; admissible-region sampling.
2. **Inference:** calibrated false-alarm rates for archive-scale searches; hierarchical models for populations (free-floating planets, ISOs).
3. **Instrument physics:** realistic noise models for TESS, WISE/NEOWISE, LOFAR and survey astrometry.
4. **Code review:** the `fdastro` package welcomes tests and independent re-derivations. See [CONTRIBUTING.md](../../CONTRIBUTING.md).
5. **Teaching:** the [university lab](../lessons/l13-university-lab-orbit-fitting.md) and the [tutorials](../tutorials/) need reviewers.

## References

- Chernoff, H. (1954). On the distribution of the likelihood ratio. *Annals of Mathematical Statistics*, 25, 573–578.
- Kipping, D. M. (2009). Transit timing effects due to an exomoon. *Monthly Notices of the Royal Astronomical Society*, 392, 181–189.
- Milani, A., et al. (2004). Orbit determination with very short arcs. I. Admissible regions. *Celestial Mechanics and Dynamical Astronomy*, 90, 57–85.
- Murray, C. D., & Dermott, S. F. (1999). *Solar System Dynamics*. Cambridge University Press.
- Paczyński, B. (1986). Gravitational microlensing by the galactic halo. *The Astrophysical Journal*, 304, 1–5.
- Self, S. G., & Liang, K.-Y. (1987). *Journal of the American Statistical Association*, 82, 605–610.
- Virtanen, J., Muinonen, K., & Bowell, E. (2001). Statistical ranging of asteroid orbits. *Icarus*, 154, 412–431.
- Will, C. M. (2014). The confrontation between general relativity and experiment. *Living Reviews in Relativity*, 17, 4.
- Abbott, B. P., et al. (2017). *The Astrophysical Journal Letters*, 848, L13 (GW170817 and GRB 170817A).
- Yee, S. W., et al. (2026). A TESS disappearing act: the vanishing transits of TOI-2535 b. *The Astrophysical Journal Letters*.
