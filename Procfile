
web: python3 terribleblooms_project/manage.py collectstatic --noinput; gunicorn terribleblooms_project.wsgi --workers=4 --bind=0.0.0.0:$PORT terribleblooms_project/settings.py 
