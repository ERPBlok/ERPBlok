from erpblok.blok import Blok
from anyblok_pyramid import PERM_WRITE
from anyblok_io.blok import BlokImporter


def import_declaration_module(reload=None):
    from . import models
    models.import_declaration_module(reload)


class Party(Blok, BlokImporter):
    """Helper to manage all your projects"""
    version = "0.1.0"
    author = "Jean-Sébastien Suzanne"
    category = 'Party'
    required = [
        'erpblok',
    ]

    furetui = {
        "i18n": {},
        "templates": [
            "templates/party.tmpl",
        ],
    }

    @classmethod
    def import_declaration_module(cls):
        import_declaration_module()

    @classmethod
    def reload_declaration_module(cls, reload):
        import_declaration_module(reload=reload)

    def update_role(self):
        party = self.registry.Pyramid.Role.ensure_exists(
            "party",
            [
                {
                    "code": "role-admin-party",
                    "model": "Model.Party",
                    "perms": PERM_WRITE,
                },
                {
                    "code": "role-admin-party-contact",
                    "model": "Model.Party.Contact",
                    "perms": PERM_WRITE,
                },
                {
                    "code": "role-admin-party-address",
                    "model": "Model.Party.Address",
                    "perms": PERM_WRITE,
                },
                {
                    "code": "role-admin-party-category",
                    "model": "Model.Party.Category",
                    "perms": PERM_WRITE,
                },
            ],
            label="Party"
        )
        admin = self.registry.Pyramid.Role.ensure_exists("admin", [
            {
                "code": "role-admin-party-configuration",
                "model": "Model.Party.Configuration",
                "perms": PERM_WRITE,
            },
            {
                "code": "role-admin-party-configuration-company",
                "model": "Model.Party.Configuration.Company",
                "perms": PERM_WRITE,
            },
            {
                "code": "role-admin-party-sequence",
                "model": "Model.Party.Sequence",
                "perms": PERM_WRITE,
            },
        ])
        if party not in admin.children:
            admin.children.append(party)

    def update(self, latest):
        self.import_file_xml("Model.FuretUI.Space", "data", "spaces.xml")
        self.import_file_xml("Model.FuretUI.Resource", "data", "resources.xml")
        self.import_file_xml("Model.FuretUI.Menu", "data", "menus.xml")
        self.update_role()
