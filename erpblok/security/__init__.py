from anyblok.blok import Blok


def import_declaration_module(reload=None):
    from . import models

    models.import_declaration_module(reload=reload)


class Security(Blok):
    """Security's Blok class definition
    """
    version = "0.1.0"
    author = "Jean-Sébastien Suzanne"
    required = [
        'anyblok-core',
        'auth',
        'audit',
    ]

    @classmethod
    def import_declaration_module(cls):
        import_declaration_module()

    @classmethod
    def reload_declaration_module(cls, reload):
        import_declaration_module(reload=reload)
