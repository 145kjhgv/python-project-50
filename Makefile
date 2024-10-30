package-install:
	python3 -m pip install --user dist/*whl
lint:
	poetry run flake8 brain_games