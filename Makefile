DC = docker-compose -f ./docker-compose.yml

format:
	isort .
	black .
	flake8 .

build-postgres:
	docker build -f ./compose/postgres/Dockerfile -t postgres .

build-django:
	docker build -f ./compose/django/Dockerfile -t django .

start:
	${DC} up

check:
	${DC} run django flake8 .

unit-tests:
	${DC} run django python ./manage.py test -v 3
