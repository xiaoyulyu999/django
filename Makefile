run-server:
	poetry run python -m core.manage runserver

install:
	poetry install

migrate:
	poetry run python -m core.manage migrate

migrations:
	poetry run python -m core.manage makemigrations