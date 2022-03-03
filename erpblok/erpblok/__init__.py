from anyblok.blok import Blok
from anyblok_io.blok import BlokImporter
from anyblok_pyramid import PERM_WRITE


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

    furetui = {
        'i18n': {
            # 'en': en,
            # 'fr': fr,
        },
        'templates': [
            'templates/company.tmpl',
            'templates/user.tmpl',
        ],
    }

    @classmethod
    def import_declaration_module(cls):
        import_declaration_module()

    @classmethod
    def reload_declaration_module(cls, reload):
        import_declaration_module(reload=reload)

    def update(self, latest):
        self.import_file_xml('Model.FuretUI.Resource', 'data', 'resources.xml')
        self.import_file_xml('Model.FuretUI.Menu', 'data', 'menus.xml')
        self.update_admin_role()

    def update_admin_role(self):
        self.anyblok.Pyramid.Role.ensure_exists(
            "admin",
            [
                {
                    "code": "role-admin-company",
                    "model": "Model.Company",
                    "perms": PERM_WRITE,
                },
                {
                    "code": "role-admin-company-contact",
                    "model": "Model.Company.Contact",
                    "perms": PERM_WRITE,
                },
                {
                    "code": "role-admin-company-address",
                    "model": "Model.Company.Address",
                    "perms": PERM_WRITE,
                },
                {
                    "code": "role-admin-company-useraccess",
                    "model": "Model.Company.UserAccess",
                    "perms": PERM_WRITE,
                },
            ],
            label="Administrator"
        )

    @classmethod
    def pyramid_load_config(cls, config):
        config.scan(cls.__module__ + ".views")
