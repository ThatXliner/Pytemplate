PYTHON := python3

test:
	@pytest tests/ -vvv --durations=3
deps:
	@$(PYTHON) -m pip install -r requirements.txt || $(PYTHON) -m ensurepip && $(PYTHON) -m pip install -r requirements.txt

dev-deps:
	@$(PYTHON) -m pip install -r dev-requirements.txt > /dev/null || $(PYTHON) -m ensurepip && $(PYTHON) -m pip install -r dev-requirements.txt > /dev/null

build:
	@$(PYTHON) setup.py sdist bdist_wheel
clean:
	@find . -type d \( -name '__pycache__' -or -name '*.egg-info' -or -name 'dist' -or -name 'build' -or -name ".pytest_cache" \)  -exec rm -rf {} +


