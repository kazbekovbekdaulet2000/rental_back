# python manage.py makemigrations
# python manage.py migrate
# python manage.py collectstatic
# python manage.py runserver 0.0.0.0:8000
gunicorn rental_back.wsgi:application --bind 0.0.0.0:8000