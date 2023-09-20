DC = docker-compose -f ./docker-compose.yml

format:
	isort .
	black .
	flake8 .

build-django:
	docker build -f ./compose/django/Dockerfile -t django .

start:
	${DC} up

check:
	${DC} run django flake8 .

unit-tests:
	${DC} run django python ./manage.py test -v 3
