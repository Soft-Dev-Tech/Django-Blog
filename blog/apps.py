from django.apps import AppConfig
from config import settings


class BlogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'
    if settings.LANGUAGE_CODE == 'fa-ir':
        verbose_name = "ویبلاگ"
