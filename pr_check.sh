# Runs .github/workflows/pr_check.yml locally
# Improvement: convert into Makefile
uv run pytest -v
uv run black --check $(git ls-files '*.py')
uv run pylint $(git ls-files '*.py')
