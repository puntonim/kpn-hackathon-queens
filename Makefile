
install:
	pip install -r requirements.txt
	python manage.py migrate

go:
	python manage.py runserver 0.0.0.0:8080
