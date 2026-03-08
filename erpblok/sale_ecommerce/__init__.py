from anyblok.blok import Blok


def import_declaration_module(reload=None):
    from . import models

    models.import_declaration_module(reload=reload)


class SaleEcommerce(Blok):
    """Sale Ecommerce's Blok class definition
    """
    version = "0.1.0"
    author = "Jean-Sébastien Suzanne"
    required = [
        'anyblok-core',
        'sale',
    ]

    @classmethod
    def import_declaration_module(cls):
        import_declaration_module()

    @classmethod
    def reload_declaration_module(cls, reload):
        import_declaration_module(reload=reload)
