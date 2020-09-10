PYTHON := python3
PROJECT_NAME := package_name

test:
	@pytest tests/ -vvv --durations=3 --cov=src/package_name
deps:
	@$(PYTHON) -m ensurepip
	@echo "Installing dependencies..."
	@$(PYTHON) -m pip install -r requirements.txt > /dev/null

dev-deps:
	@$(PYTHON) -m ensurepip
	@echo "Installing developer dependencies..."
	@$(PYTHON) -m pip install -r dev-requirements.txt > /dev/null

build:
	@$(PYTHON) setup.py sdist bdist_wheel

clean:
	@$(PYTHON) -m ensurepip
	@find . -type d \( -name '__pycache__' -or -name '*.egg-info' -or -name 'dist' -or -name 'build' -or -name '.pytest_cache' \)  -exec rm -rf {} +
	@black . || @$(PYTHON) -m pip install black > /dev/null || @echo "Black failed."
develop:
	@$(PYTHON) -m ensurepip
	@$(PYTHON) setup.py sdist bdist_wheel
	@$(PYTHON) -m pip install -e .
	
