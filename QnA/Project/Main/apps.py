#allows to use the subclasses of app anywhere
from django.apps import AppConfig


class MainConfig(AppConfig):
    name = 'Main'
