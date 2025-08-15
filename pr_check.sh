# Runs .github/workflows/pr_check.yml locally
# Improvement: convert into Makefile
python3 -m unittest src/tests/test_*.py -v -c
uv run black --check $(git ls-files '*.py')
uv run pylint $(git ls-files '*.py')
