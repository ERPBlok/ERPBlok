from anyblok.blok import Blok
from anyblok_io.blok import BlokImporter


def import_declaration_module(reload=None):
    from . import models

    models.import_declaration_module(reload)


class BlokManager(Blok, BlokImporter):
    """ERPBlok.project.short_description"""
    version = "0.1.0"
    author = "Jean-Sébastien Suzanne"
    required = [
        'erpblok',
    ]

    furetui = {
        "templates": [
            "templates/blok.tmpl",
        ],
    }

    @classmethod
    def import_declaration_module(cls):
        import_declaration_module()

    @classmethod
    def reload_declaration_module(cls, reload):
        import_declaration_module(reload=reload)

    def update(self, latest):
        self.import_file_xml("Model.FuretUI.Resource", "data", "resources.xml")
        self.import_file_xml("Model.FuretUI.Menu", "data", "menus.xml")
