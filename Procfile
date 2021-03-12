
web: python3 terribleblooms_project/manage.py collectstatic --noinput; bin/gunicorn_django --workers=4 --bind=0.0.0.0:$PORT terribleblooms_project/settings.py 
