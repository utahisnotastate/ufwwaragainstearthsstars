# Contributing

Thank you for helping! This project welcomes contributions from students, teachers, amateur astronomers and professionals alike.

## For young contributors

If you are under 18, please ask a parent, guardian or teacher to help you take part. They should create any accounts. Never post your full name, school, address or photos.

## Ways to help

- **Fix a mistake** in a page or a number. (Please include a source.)
- **Make a page easier to read** for kids, or add a picture with good alt text.
- **Translate** a lesson or disclosure.
- **Improve the code** or add tests.
- **Try a tutorial** and tell us where you got stuck.
- **Propose a new disclosure** using the issue template.
- **Report a candidate** you found — but first read [how to report a discovery](docs/about/how-to-report-a-discovery.md).

## Writing rules

All writing follows the [style guide](docs/STYLE.md). The short version:

1. Start every page with a simple part a 10-year-old can read; put equations under "For experts".
2. Label every claim with an evidence level (Confirmed, Strong evidence, Testable idea, Long shot).
3. Cite real, checkable sources. Never invent a reference.
4. Be respectful. No hype, no "scientists are hiding it", no science-fiction framing, no health claims.

## Code rules

- Python 3.11+, `numpy` and `scipy` only in the core. Optional archive tools go behind the `archives` extra.
- Every new function needs a test. Run the suite with:

  ```bash
  python -m pytest
  ```

- In `docs/tutorials/`, every block fenced as `python` is executed by `tests/test_docs_snippets.py`. Fence examples that need the internet or optional packages as `py` instead.
- Public functions need docstrings with a short "For young readers" explanation in the module docstring and the math under "For experts".
- Results must never say "confirmed". Use "candidate" and report significance honestly.

## Pull request checklist

- [ ] Tests pass (`python -m pytest`).
- [ ] New claims have an evidence level and a reference.
- [ ] The simple layer is still simple.
- [ ] Links work.
- [ ] I added a line to [CHANGELOG.md](CHANGELOG.md) for anything user-visible.

## Review

Science changes get at least one reviewer with relevant expertise. Lessons for young children get a reviewer with teaching experience. See the review process in the [disclosure plan](docs/plan/disclosure-plan.md).

By contributing, you agree that your code is released under the MIT License and your writing under CC BY 4.0.
