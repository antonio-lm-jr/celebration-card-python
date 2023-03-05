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
	@flake8 --show-source src/

_isort:
	@isort --check-only src/

_black:
	@black --diff --check src/

_isort-fix:
	@isort src/ tests/

_black-fix:
	@black src/ tests/

_mypy:
	@mypy src/

lint: _flake8 _isort _black _mypy
format-code: _isort-fix _black-fix

# Test
test-cov: clean
	@pytest tests/ --cov src
