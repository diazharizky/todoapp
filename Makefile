.PHONY: migrate create_user run_server make_migrations

PYTHON_MANAGE=python manage.py

migrate:
	$$(echo $(PYTHON_MANAGE)) migrate

create_user:
	$$(echo $(PYTHON_MANAGE)) createsuperuser

run_server:
	$$(echo $(PYTHON_MANAGE)) runserver

make_migrations:
	$$(echo $(PYTHON_MANAGE)) makemigrations
