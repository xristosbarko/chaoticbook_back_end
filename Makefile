DC = docker-compose -f ./docker-compose.yml

format:
	isort .
	black .
	flake8 .

build-postgres:
	docker build -f ./compose/postgres/Dockerfile -t postgres .

build-django:
	docker build -f ./compose/django/Dockerfile -t django .

up:
	${DC} run django sh -c "python ./manage.py migrate && python ./manage.py runserver 0.0.0.0:8000"

check:
	${DC} run django flake8 .

unit-tests:
	${DC} run django python ./manage.py test -v 3
