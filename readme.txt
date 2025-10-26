# Terrible Blooms

A Django web application for managing and streaming audio plays.

## Local Development Setup

### Prerequisites
- Python 3.9.18 or higher
- PostgreSQL
- pip (package installer for Python)

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
python -m pip install --upgrade pip

# Install project dependencies
pip install -r requirements.txt
```

### Step 4: Set Up Environment Variables
Create a `.env` file in the root directory with the following variables:
```
DEBUG="True"
SECRET_KEY="your-secret-key-here"
CLOUD_NAME="your-cloudinary-cloud-name"
API_KEY="your-cloudinary-api-key"
API_SECRET="your-cloudinary-api-secret"
```

To generate a new secret key:
```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

### Step 5: Set Up PostgreSQL Database
```bash
# Create the database
createdb terribleblooms

# Run migrations
python manage.py migrate
```

### Step 6: Run the Development Server
```bash
python manage.py runserver
```
The site will be available at http://localhost:8000

### Step 7: Create Superuser (Optional)
To access the admin interface:
```bash
python manage.py createsuperuser
```

## File Upload Limits
- Maximum file size: 100MB
- Supported formats: Audio files for plays, images for artwork
- Large file uploads are handled in chunks of 10MB
- Upload timeout: 10 minutes

## Deployment Notes
When deploying to Heroku, set these additional configs:
```bash
heroku config:set NGINX_UPLOAD_LIMIT=100M
heroku config:set UPLOAD_MAX_FILE_SIZE=100000000
```

## Cloudinary Setup
1. Sign up for a Cloudinary account at https://cloudinary.com
2. Get your cloud name, API key, and API secret from your dashboard
3. Add these to your .env file as shown above

## Common Issues
- If uploads timeout, check your internet connection stability
- For files larger than 100MB, they will need to be compressed first
- Make sure your Cloudinary account has enough storage space

## Tech Stack
- Django 3.2.23 (LTS)
- PostgreSQL
- Cloudinary for media storage
- Whitenoise for static files
- Gunicorn for production server

## Security Notes
For local development, SSL redirect and secure cookie settings are disabled by default. In production, these security features are automatically enabled.
