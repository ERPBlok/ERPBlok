from anyblok.blok import Blok
from anyblok_io.blok import BlokImporter


def import_declaration_module(reload=None):
    from . import models

    models.import_declaration_module(reload)


class Erpblok(Blok, BlokImporter):
    """Erpblok's Blok class definition
    """
    version = "0.1.0"
    author = "Jean-Sébastien Suzanne"
    required = [
        'anyblok-core',
        'furetui',
        "furetui-auth",
    ]

    @classmethod
    def import_declaration_module(cls):
        import_declaration_module()

    @classmethod
    def reload_declaration_module(cls, reload):
        import_declaration_module(reload=reload)

    def update(self, latest):
        """Update blok"""

    @classmethod
    def pyramid_load_config(cls, config):
        config.scan(cls.__module__ + ".views")
