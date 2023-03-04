.PHONY=help

clean:
	@find . -name "*.pyc" | xargs rm -rf
	@find . -name "__pycache__" -type d | xargs rm -rf

# Dependencies
_base_pip:
	@pip install -U pip poetry wheel

dev-dependencies: _base_pip
	@poetry install


# Run
run:
	@uvicorn src.main:app --port 3000 --reload


# Lint
_flake8:
	@flake8 --show-source .

_isort:
	@isort --diff --check-only src/

_black:
	@black --check src/

_isort-fix:
	@isort src/

_black_fix:
	@black src/

_mypy:
#	@mypy src/

lint: _isort _black _mypy
format-code: _isort-fix _black_fix

# Test
test-cov: clean
	@pytest -v tests/
