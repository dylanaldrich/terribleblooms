# Quick Reference Guide

## Local Development
```bash
# Start development server
DEVELOPMENT=true venv/bin/python manage.py runserver 8080

# Access at
http://localhost:8080
```

## Common Commands
```bash
# Run migrations
venv/bin/python manage.py migrate

# Create superuser
venv/bin/python manage.py createsuperuser

# Collect static files
venv/bin/python manage.py collectstatic

# Run tests
venv/bin/python manage.py test

# Check for issues
venv/bin/python manage.py check --deploy
```

## Heroku Deployment
```bash
# Deploy
git push heroku heroku-upgrade-2025:main

# Run migrations
heroku run python manage.py migrate

# View logs
heroku logs --tail

# Open app
heroku open
```

## Heroku Config
```bash
# View all config
heroku config

# Set config variable
heroku config:set KEY=value

# Unset config variable
heroku config:unset KEY
```

## Database
```bash
# Local backup
pg_dump terribleblooms > backup.sql

# Local restore
psql terribleblooms < backup.sql

# Heroku backup
heroku pg:backups:capture

# Heroku restore
heroku pg:backups:restore
```

## Troubleshooting
```bash
# Check Python version
python --version

# Check Django version
venv/bin/python -m django --version

# Check installed packages
venv/bin/pip list

# Check Heroku status
heroku ps

# Restart Heroku dyno
heroku restart
```

For full documentation, see README.md
