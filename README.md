# A Garden of Terrible Blooms

A Django web application for managing and streaming short plays of the weird and surreal set in Los Angeles.

## 📋 Table of Contents
- [Tech Stack](#tech-stack)
- [Prerequisites](#prerequisites)
- [Local Development Setup](#local-development-setup)
- [Heroku Deployment](#heroku-deployment)
- [Configuration](#configuration)
- [Common Issues](#common-issues)

## 🛠 Tech Stack

- **Backend**: Django 3.2.23 (LTS)
- **Database**: PostgreSQL
- **Media Storage**: Cloudinary
- **Static Files**: WhiteNoise
- **Production Server**: Gunicorn
- **Deployment**: Heroku

## 📦 Prerequisites

- Python 3.7 or higher
- PostgreSQL
- Git
- Heroku CLI (for deployment)
- Cloudinary account (free tier available)

## 🚀 Local Development Setup

### Step 1: Clone the Repository
```bash
git clone https://github.com/dylanaldrich/terribleblooms.git
cd terribleblooms
```

### Step 2: Set Up Virtual Environment
```bash
# Create a virtual environment
python3 -m venv venv

# Activate the virtual environment
# On macOS/Linux:
source venv/bin/activate
# On Windows:
# venv\Scripts\activate
```

### Step 3: Install Dependencies
```bash
# Upgrade pip first
venv/bin/python -m pip install --upgrade pip

# Install project dependencies
venv/bin/python -m pip install -r requirements.txt
```

### Step 4: Set Up Environment Variables
Create a `.env` file in the root directory:
```bash
DEBUG=True
DEVELOPMENT=true
SECRET_KEY="your-secret-key-here"
CLOUD_NAME="your-cloudinary-cloud-name"
API_KEY="your-cloudinary-api-key"
API_SECRET="your-cloudinary-api-secret"
```

**Generate a new Django secret key:**
```bash
venv/bin/python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

### Step 5: Create Development Marker File
```bash
# Create an empty .development file to trigger development mode
touch .development
```

### Step 6: Set Up PostgreSQL Database
```bash
# Create the database
createdb terribleblooms

# Run migrations
venv/bin/python manage.py migrate
```

### Step 7: Create Superuser (Optional)
To access the admin interface at `/admin`:
```bash
venv/bin/python manage.py createsuperuser
```

### Step 8: Run the Development Server
```bash
# Always use port 8080 for local development
DEVELOPMENT=true venv/bin/python manage.py runserver 8080
```

🌐 Access the application at: **http://localhost:8080**

> **Note**: Use port 8080 instead of 8000 to avoid HSTS browser cache issues.

## 🚢 Heroku Deployment

### Initial Setup

#### 1. Install Heroku CLI
```bash
# macOS
brew tap heroku/brew && brew install heroku

# Or download from: https://devcenter.heroku.com/articles/heroku-cli
```

#### 2. Login to Heroku
```bash
heroku login
```

#### 3. Create Heroku App
```bash
# Create a new Heroku app
heroku create your-app-name

# Or link to existing app
heroku git:remote -a your-app-name
```

#### 4. Add PostgreSQL Database
```bash
heroku addons:create heroku-postgresql:mini
```

### Configure Environment Variables

Set all required environment variables on Heroku:

```bash
# Django Settings
heroku config:set SECRET_KEY="your-production-secret-key"
heroku config:set DEBUG=False
heroku config:set ALLOWED_HOSTS="your-app-name.herokuapp.com,www.terribleblooms.net,terribleblooms.net"

# Cloudinary Settings
heroku config:set CLOUD_NAME="your-cloudinary-cloud-name"
heroku config:set API_KEY="your-cloudinary-api-key"
heroku config:set API_SECRET="your-cloudinary-api-secret"

# Security Settings (automatically enabled in production)
heroku config:set SECURE_SSL_REDIRECT=True
heroku config:set SESSION_COOKIE_SECURE=True
heroku config:set CSRF_COOKIE_SECURE=True

# File Upload Settings
heroku config:set NGINX_UPLOAD_LIMIT=100M
heroku config:set UPLOAD_MAX_FILE_SIZE=100000000

# Ensure DEVELOPMENT is NOT set in production
heroku config:unset DEVELOPMENT
```

**Verify configuration:**
```bash
heroku config
```

### Deploy to Heroku

```bash
# Ensure you're on the correct branch
git checkout heroku-upgrade-2025

# Deploy to Heroku
git push heroku heroku-upgrade-2025:main

# Run database migrations
heroku run python manage.py migrate

# Collect static files
heroku run python manage.py collectstatic --noinput

# Create a superuser (if needed)
heroku run python manage.py createsuperuser
```

### Monitor Your Deployment

```bash
# View logs
heroku logs --tail

# Check deployment status
heroku ps

# Run Django check
heroku run python manage.py check --deploy
```

### Update Deployment

```bash
# After making changes, commit and push
git add .
git commit -m "Your commit message"
git push heroku heroku-upgrade-2025:main

# Run migrations if models changed
heroku run python manage.py migrate
```

## ⚙️ Configuration

### Development Mode Features
- ✅ Disabled SSL/HTTPS redirects
- ✅ Minimal middleware for faster development
- ✅ Local PostgreSQL database
- ✅ Debug mode enabled
- ✅ CORS allows all origins
- ✅ Detailed error pages

### Production Mode Features
- 🔒 Full SSL/HTTPS security
- 🔒 HSTS headers (1 year)
- ⚡ Rate limiting middleware
- ⚡ Gzip compression
- ⚡ Page caching (5-60 minutes)
- ⚡ Static file compression (WhiteNoise)
- 📦 Cloudinary for media storage
- 🛡️ Restricted CORS origins
- 🎨 Custom error pages (400, 403, 404, 500)

### File Upload Limits
- **Maximum file size**: 100MB
- **Supported formats**: Audio files for plays, images for artwork
- **Chunk size**: 10MB for large uploads
- **Upload timeout**: 10 minutes

### Cloudinary Setup
1. Sign up for a free account at [cloudinary.com](https://cloudinary.com)
2. Get your credentials from the dashboard
3. Add to `.env` (local) or Heroku config (production)

## 🐛 Common Issues

### Local Development

**Issue: HTTPS errors on localhost**
- **Solution**: Use port 8080 instead of 8000
- **Command**: `DEVELOPMENT=true venv/bin/python manage.py runserver 8080`

**Issue: Static files not loading**
- **Solution**: Make sure the `.development` file exists
- **Command**: `touch .development`

**Issue: Database connection errors**
- **Solution**: Ensure PostgreSQL is running and database exists
- **Command**: `createdb terribleblooms`

**Issue: Missing environment variables**
- **Solution**: Check your `.env` file has all required variables
- **Reference**: See `.env.example` for template

### Production Deployment

**Issue: Static files not found (404)**
```bash
heroku run python manage.py collectstatic --noinput
```

**Issue: Database migrations not applied**
```bash
heroku run python manage.py migrate
```

**Issue: 500 Internal Server Error**
```bash
# Check logs for details
heroku logs --tail

# Ensure DEBUG=False in production
heroku config:get DEBUG
```

**Issue: Large file uploads failing**
```bash
# Increase Heroku timeout
heroku config:set NGINX_UPLOAD_LIMIT=100M
```

## 🔐 Security Notes

### Development
- SSL redirect and secure cookies are **disabled**
- CORS allows all origins for testing
- Debug mode shows detailed error pages
- Never commit `.env` files to Git

### Production
- SSL/HTTPS is **enforced**
- HSTS headers prevent downgrade attacks
- Secure cookies (session & CSRF)
- CORS restricted to specific domains
- Rate limiting prevents abuse
- Custom error pages hide sensitive info

## 📁 Important Files

- `manage.py` - Django management script
- `requirements.txt` - Python dependencies
- `Procfile` - Heroku process configuration
- `runtime.txt` - Python version for Heroku
- `.env` - Local environment variables (not in Git)
- `.env.example` - Template for environment variables
- `.development` - Marker file for development mode
- `PRODUCTION_IMPROVEMENTS.md` - Detailed changelog

## 📚 Additional Resources

- [Django Documentation](https://docs.djangoproject.com/en/3.2/)
- [Heroku Python Support](https://devcenter.heroku.com/articles/python-support)
- [Cloudinary Django Integration](https://cloudinary.com/documentation/django_integration)
- [WhiteNoise Documentation](http://whitenoise.evans.io/)

## 📝 License

Copyright © 2025 A Garden of Terrible Blooms

## 👤 Authors

- **Dylan Aldrich** - Web Design & Development
- [dylanaldrich.com](https://dylanaldrich.com)

## 🌐 Live Site

[www.terribleblooms.net](https://www.terribleblooms.net)
