.PHONY: clean clean-build clean-pyc lint test setup help
.DEFAULT_GOAL := help

define PRINT_HELP_PYSCRIPT
import re, sys

for line in sys.stdin:
	match = re.match(r'^([a-zA-Z_-]+):.*?## (.*)$$', line)
	if match:
		target, help = match.groups()
		print("%-20s %s" % (target, help))
endef
export PRINT_HELP_PYSCRIPT

help:
	@python -c "$$PRINT_HELP_PYSCRIPT" < $(MAKEFILE_LIST)

setup: ## install python project dependencies
	pip install --upgrade pip wheel
	pip install --upgrade -r requirements.txt
	python update_project.py -c app.cfg

setup-tests: ## install python project dependencies for tests
	pip install --upgrade pip wheel
	pip install --upgrade -r requirements.test.txt
	python update_project.py -c app.test.cfg
	nodeenv -p
	npm i -g npm
	npm install

setup-dev: ## install python project dependencies for development
	pip install --upgrade pip wheel
	pip install --upgrade -r requirements.dev.txt
	python update_project.py -c app.dev.cfg --with-demo
	nodeenv -p
	npm i -g npm
	npm install

run-dev: ## launch pyramid development server
	anyblok_pyramid -c app.dev.cfg --wsgi-host 0.0.0.0

run-gunicorn: ## launch pyramid server with gunicorn
	gunicorn_anyblok_pyramid --anyblok-configfile app.cfg
run-dev-npm: ## launch npm development server with hot reload
	npm update
	npm run serve

build-assets: ## build js and scss assets for production
	npm update
	npm run build
	rm -rfv erpblok/erpblok/static/furetui
	mv dist erpblok/erpblok/static/furetui


clean: clean-build clean-pyc clean-test ## remove all build, test, coverage and Python artifacts

clean-build: ## remove build artifacts
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -f {} +

clean-pyc: ## remove Python file artifacts
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean-test: ## remove test artifacts
	rm -fr htmlcov
	rm -fr .pytest_cache
	rm -f .coverage

lint: ## check style with flake8
	flake8 erpblok
	npm run lint

test: ## run tests
	ANYBLOK_CONFIG_FILE=app.test.cfg py.test -v -s erpblok
	# npm run test:unit

documentation: ## generate documentation
	anyblok_doc -c app.test.cfg --doc-format RST --doc-output doc/source/apidoc.rst
	make -C doc/ html
