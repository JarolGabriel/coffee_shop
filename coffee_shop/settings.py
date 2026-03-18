import os
from pathlib import Path

import dj_database_url
import environ

BASE_DIR = Path(__file__).resolve().parent.parent
env = environ.Env()

env_file = os.path.join(BASE_DIR, ".env")
if os.path.exists(env_file):
    environ.Env.read_env(env_file)

# --- SEGURIDAD ---
SECRET_KEY = env("SECRET_KEY", default="django-insecure-tu-clave-aqui")
DEBUG = env.bool("DEBUG", default=True)  # Mantenlo en True hasta que cargue la web
ALLOWED_HOSTS = ["*"]
CSRF_TRUSTED_ORIGINS = [
    "https://coffeeshop-production-87be.up.railway.app",
    "http://localhost:8000",
]
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

# --- APLICACIONES ---
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "cloudinary_storage",
    "django.contrib.staticfiles",
    "cloudinary",
    "crispy_forms",
    "crispy_tailwind",
    "products",
    "users",
    "orders",
    "rest_framework",
    "widget_tweaks",
]

# --- MIDDLEWARE ---
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",  # Debe ir aquí
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "coffee_shop.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
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

WSGI_APPLICATION = "coffee_shop.wsgi.application"

# --- BASE DE DATOS (REPARADO) ---
if env("DJANGO_DB_URL", default=None):
    DATABASES = {"default": dj_database_url.config(default=env("DJANGO_DB_URL"))}
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }

# --- ARCHIVOS ESTÁTICOS Y CLOUDINARY (REPARADO) ---
STATIC_URL = "static/"
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_DIRS = [BASE_DIR / "static"]

# Configuración de Cloudinary
CLOUDINARY_STORAGE = {
    "CLOUD_NAME": env("CLOUDINARY_CLOUD_NAME", default="dkenfgg3z"),
    "API_KEY": env("CLOUDINARY_API_KEY", default="145769945712436"),
    "API_SECRET": env("CLOUDINARY_API_SECRET", default="6F9Wjlzi64ZvWoo9Uv8cFsm7SGE"),
}

# Almacenamiento para Django 5.x
STORAGES = {
    "default": {
        "BACKEND": "cloudinary_storage.storage.MediaCloudinaryStorage",
    },
    "staticfiles": {
        "BACKEND": "whitenoise.storage.StaticFilesStorage",
    },
}

# --- OTROS ---
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
CRISPY_ALLOWED_TEMPLATE_PACKS = "tailwind"
CRISPY_TEMPLATE_PACK = "tailwind"
LOGIN_REDIRECT_URL = "product_list"
LOGOUT_REDIRECT_URL = "/usuarios/login/"
