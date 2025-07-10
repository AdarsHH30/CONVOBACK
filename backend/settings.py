from pathlib import Path
import os
import dotenv
from asgiref.sync import async_to_sync

BASE_DIR = Path(__file__).resolve().parent.parent
# Environment
dotenv.load_dotenv(BASE_DIR / ".env")
# Port configuration
PORT = int(os.getenv("PORT", "8000"))
SECRET_KEY = os.getenv("PRODUCTION_KEY", "django-insecure-fallback-key")
FRONTEND_URL = os.getenv("FRONTEND_URL", "http://localhost:5173").rstrip("/")


# ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", "").split(",")
# ALLOWED_HOSTS = [host.strip() for host in ALLOWED_HOSTS if host.strip()]
ALLOWED_HOSTS = "127.0.0.1:8000,127.0.0.1,localhost,convoback-1.onrender.com".split(",")


CORS_ALLOWED_ORIGINS = [FRONTEND_URL]
CORS_ALLOW_ALL_ORIGINS = False
CORS_ALLOW_CREDENTIALS = True

CSRF_TRUSTED_ORIGINS = [FRONTEND_URL]

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


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}
# Disable auth and migrations
AUTH_PASSWORD_VALIDATORS = []
MIGRATION_MODULES = {
    "auth": None,
    "contenttypes": None,
    "admin": None,
    "sessions": None,
}
WSGI_APPLICATION = "backend.asgi.application"

# ASGI/Channels
ASGI_APPLICATION = "backend.asgi.application"
REDIS_URL = os.environ.get("redis_host", "redis://localhost:6379/0")

CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            "hosts": [REDIS_URL],
        },
    },
}

# # Test Redis connection
# import channels.layers

# try:
#     channel_layer = channels.layers.get_channel_layer()
#     async_to_sync(channel_layer.send)("test_channel", {"type": "test.message"})
#     print("Redis connection successful")
# except Exception as e:
#     print(f"Redis connection failed: {e}")


MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "backend.urls"
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
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
DEBUG = os.getenv("DEBUG", "False")

# ---
# Additional production security recommendations:
# - Set SECURE_SSL_REDIRECT = True
# - Set SESSION_COOKIE_SECURE = True
# - Set CSRF_COOKIE_SECURE = True
# - Set X_FRAME_OPTIONS = 'DENY' or 'SAMEORIGIN'
# - Set SECURE_HSTS_SECONDS = 31536000
# - Set SECURE_HSTS_INCLUDE_SUBDOMAINS = True
# - Set SECURE_HSTS_PRELOAD = True
# Uncomment and configure the above as needed for your deployment.
