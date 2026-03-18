release: python manage.py migrate
web: python manage.py collectstatic --noinput && gunicorn coffee_shop.wsgi --bind 0.0.0.0:$PORT --log-file -