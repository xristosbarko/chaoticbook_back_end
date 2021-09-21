DC = docker-compose -f ./docker-compose.yml

format:
	isort .
	black .
	flake8 .

build-postgres:
	docker build -f ./compose/postgres/Dockerfile -t postgres .

build-django:
	docker build -f ./compose/django/Dockerfile -t django .

build-postgres-pi:
	docker buildx build --platform linux/arm64 -f ./compose/postgres/Dockerfile -t postgres .

build-django-pi:
	docker buildx build --platform linux/arm64 -f ./compose/django/Dockerfile-pi -t django .

start:
	${DC} up

check:
	${DC} run django flake8 .

unit-tests:
	${DC} run django python ./manage.py test -v 3
