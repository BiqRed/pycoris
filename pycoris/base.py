from pycoris.settings import BaseSettings
from typing import Type, Optional


class Pycoris:
    def __init__(self, settings: Optional[Type[BaseSettings]] = None):
        if settings is not None and type(settings) is not type:
            raise TypeError(f'settings must BaseSettings, not {type(settings)}')
        self.settings = settings or BaseSettings
        self.settings.validate()


BaseSettings.secret_key = 'pycoris'*3
pycoris = Pycoris()
