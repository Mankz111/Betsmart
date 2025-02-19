from django.apps import AppConfig


class BetsmartappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'betsmartapp'
    def ready(self):
        import betsmartapp.signals
