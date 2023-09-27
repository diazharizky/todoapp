.PHONY: migrate create_user run make_migrations

PYTHON_MANAGE=python manage.py

migrate:
	$$(echo $(PYTHON_MANAGE)) migrate

create_user:
	$$(echo $(PYTHON_MANAGE)) createsuperuser

run:
	$$(echo $(PYTHON_MANAGE)) runserver

make_migrations:
	$$(echo $(PYTHON_MANAGE)) makemigrations

lint:
	ruff check .
