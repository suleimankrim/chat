from django.apps import AppConfig


class CodefindConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'codefind'

    def ready(self):
        import codefind.signals
