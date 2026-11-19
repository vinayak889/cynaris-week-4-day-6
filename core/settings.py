import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY", "local-dev-only-key-change-me")
DEBUG = os.environ.get("DJANGO_DEBUG", "false").lower() == "true"
ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS", "localhost,127.0.0.1,0.0.0.0").split(",")
INSTALLED_APPS = ["django.contrib.contenttypes", "django.contrib.staticfiles", "app"]
MIDDLEWARE = ["django.middleware.security.SecurityMiddleware"]
ROOT_URLCONF = "core.urls"
TEMPLATES = []
WSGI_APPLICATION = "core.wsgi.application"
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ.get("POSTGRES_DB", "cicd_demo"),
        "USER": os.environ.get("POSTGRES_USER", "cicd_user"),
        "PASSWORD": os.environ.get("POSTGRES_PASSWORD", "dev-password-change-me"),
        "HOST": os.environ.get("DB_HOST", "db"),
        "PORT": os.environ.get("DB_PORT", "5432"),
    }
}
STATIC_URL = "static/"
STATIC_ROOT = BASE_DIR / "staticfiles"
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
