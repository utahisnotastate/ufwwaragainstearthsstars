"""Run every ```python block in the tutorials, so documentation cannot drift from the code.

Blocks fenced as ```py (network or optional packages) are skipped. Blocks in one
file share a namespace and run in order, like a notebook.
"""

from __future__ import annotations

import re
from pathlib import Path

import pytest

TUTORIALS = Path(__file__).resolve().parents[1] / "docs" / "tutorials"
BLOCK = re.compile(r"^```python\n(.*?)^```", re.S | re.M)


def _tutorial_files():
    return sorted(p for p in TUTORIALS.glob("t*.md"))


@pytest.mark.parametrize("path", _tutorial_files(), ids=lambda p: p.name)
def test_tutorial_python_blocks_run(path: Path, capsys):
    blocks = BLOCK.findall(path.read_text(encoding="utf-8"))
    namespace: dict = {"__name__": f"tutorial_{path.stem}"}
    for i, code in enumerate(blocks, start=1):
        try:
            exec(compile(code, f"{path.name}[block {i}]", "exec"), namespace)
        except Exception as exc:  # pragma: no cover - failure path reports context
            pytest.fail(f"{path.name} block {i} failed: {exc!r}\n---\n{code}")
    capsys.readouterr()
