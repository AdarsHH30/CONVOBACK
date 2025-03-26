from pathlib import Path
import os
import dotenv

BASE_DIR = Path(__file__).resolve().parent.parent

# Environment
dotenv.load_dotenv(BASE_DIR / ".env")
SECRET_KEY = os.getenv("PRODUCTION_KEY", "django-insecure-fallback-key")

# Security
DEBUG = True
ALLOWED_HOSTS = ["*"]
CORS_ALLOW_ALL_ORIGINS = True

# # Applications (minimal setup)
# INSTALLED_APPS = [
#     # Remove these:
#     # 'django.contrib.admin',
#     # 'django.contrib.auth',
#     # 'django.contrib.contenttypes',
#     # 'django.contrib.sessions',
#     # Keep these:
#     "daphne",
#     "channels",
#     "corsheaders",
#     "api",
#     "django.contrib.staticfiles",
# ]

INSTALLED_APPS = [
    "daphne",
    "channels",
    "corsheaders",
    "api",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]
# Disable database completely
DATABASES = {}
DEFAULT_AUTO_FIELD = None

# Disable auth and migrations
AUTH_PASSWORD_VALIDATORS = []
MIGRATION_MODULES = {
    "auth": None,
    "contenttypes": None,
    "admin": None,
    "sessions": None,
}

# ASGI/Channels
ASGI_APPLICATION = "backend.asgi.application"
CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels.layers.InMemoryChannelLayer",
    },
}

# Middleware (simplified)
MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.security.SecurityMiddleware",
]

# URLs and templates
ROOT_URLCONF = "backend.urls"
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
            ],
        },
    },
]

# Internationalization
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

# Static files
STATIC_URL = "static/"
