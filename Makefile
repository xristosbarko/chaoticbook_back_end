format:
	isort .
	black .
	flake8 .

check:
	flake8 .