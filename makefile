# makefile

install:
	poetry install
	
build:
	poetry build
	
publish:
	poetry publish --dry-run
	
package-install:
	poetry run pip install --user dist/*.whl

package-install-reinstall:
	poetry run pip install --user dist/*.whl --force-reinstall

lint:
	poetry run flake8

update:
	poetry update

test:
	poetry run pytest

extended-test:
	poetry run pytest -vv

test-cov:
	poetry run pytest --cov