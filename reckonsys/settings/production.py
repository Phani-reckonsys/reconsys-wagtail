from .base import *

DEBUG = False

# All the hosts to allow
http_hosts = (
    "localhost:8000",
    "127.0.0.1:8000",
    "localhost",
    "127.0.0.1",
    # EC2 IP
    "172.31.26.146",
)
https_hosts = (
    "qa.reckonsys.com",
    "www.reckonsys.com",
    "reckonsys.com",
)
if alb_url := env.get("ALB_URL"):
    https_hosts = (alb_url,) + https_hosts

# Set secret keys and allowed hosts
SECRET_KEY = env.get(
    "DJANGO_SECRET_KEY",
    "django-insecure-ln3v$i&2-^obg&qxik*c#g@yj+brr$h+f10dg1&797$jvd0ifg",
)
ALLOWED_HOSTS = list(http_hosts + https_hosts)

# Cors Alowed hosts
CORS_ALLOWED_ORIGINS = [f"http://{host}" for host in http_hosts]
CORS_ALLOWED_ORIGINS += [f"https://{host}" for host in https_hosts]

# CSRF Settings
CSRF_TRUSTED_ORIGINS = CORS_ALLOWED_ORIGINS[:]
USE_X_FORWARDED_HOST = True

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
ADMINS = [("tejesh", "tejesh@reckonsys.com")]


# Rest Framework, disable browsable API
REST_FRAMEWORK["DEFAULT_RENDERER_CLASSES"] = ("rest_framework.renderers.JSONRenderer",)
