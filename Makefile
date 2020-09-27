clean:
	@find ./ -name '*.pyc' -exec rm -f {} \;
	@find ./ -name 'Thumbs.db' -exec rm -f {} \;
	@find ./ -name '*~' -exec rm -f {} \;
	rm -rf .cache
	rm -rf build
	rm -rf dist
	rm -rf *.egg-info
	rm -rf htmlcov
	rm -rf .tox/
	rm -rf docs/_build
	pip3 install -e .[dev] --upgrade --no-cache

install:
	pip3 install -e .['dev']

test:
	FLASK_ENV=test pytest tests/ -v --cov=gestao_pos

run-dev:
	FLASK_APP=gestao_pos/app.py FLASK_ENV=development flask run

run-prod:
	FLASK_ENV=production gunicorn gestao_pos.wsgi --timeout 120 -w 3 -b 0.0.0.0:5000

run-shell:
	FLASK_APP=gestao_pos/app.py FLASK_ENV=production flask shell

init_db:
	FLASK_APP=gestao_pos/app.py flask create-db
	FLASK_APP=gestao_pos/app.py flask db init

format:
	isort **/*.py
	black -l 79 **/*.py