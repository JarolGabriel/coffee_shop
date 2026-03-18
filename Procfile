release: python manage.py migrate
web: python manage.py collectstatic --noinput || true && gunicorn coffee_shop.wsgi --bind 0.0.0.0:$PORT