run:
	poetry run python manage.py runserver 0.0.0.0:8000

celery:
	poetry run celery --app config.celery.app worker

run_p:
	poetry run python manage.py runserver_plus 0.0.0.0:8000

sh:
	poetry run python manage.py shell_plus

migration $(model):
	poetry run python manage.py makemigrations $(model)
	poetry run python manage.py migrate $(model)
