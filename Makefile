PYTHON := $(python3 )
PYTHONM := $($(PYTHON) -m)

test:
	@$(PYTHONM) pytest tests/ -vvv --durations=3
deps:
	@$(PYTHONM) ensurepip
	@echo "Installing dependencies..."
	@$(PYTHONM) pip install -r requirements.txt > /dev/null

dev-deps:
	@$(PYTHONM) ensurepip
	@echo "Installing developer dependencies..."
	@$(PYTHONM) pip install -r dev-requirements.txt > /dev/null

build:
	@$(PYTHON) setup.py sdist bdist_wheel

clean:
	@$(PYTHONM) ensurepip
	@find . -type d \( -name '__pycache__' -or -name '*.egg-info' -or -name 'dist' -or -name 'build' -or -name '.pytest_cache' \)  -exec rm -rf {} +
	@black . || @$(PYTHONM) pip install black > /dev/null || @echo "Black failed."
develop:
	@$(PYTHONM) ensurepip
	@$(PYTHON) setup.py sdist bdist_wheel
	@$(PYTHONM) pip install -e .
	
