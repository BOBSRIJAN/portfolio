from django.apps import AppConfig
from . import PingTest

class AppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app'
    
    def ready(self):
        PingTest.start()