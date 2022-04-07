from erpblok.blok import Blok
from anyblok_pyramid import PERM_WRITE
from anyblok_io.blok import BlokImporter


def import_declaration_module(reload=None):
    from . import models
    models.import_declaration_module(reload)


class Hr(Blok, BlokImporter):
    """Manage the Human Resource in the company"""
    version = "0.1.0"
    author = "Jean-Sébastien Suzanne"
    category = 'HR'
    required = [
        'erpblok',
    ]

    furetui = {
        "templates": [
            "templates/hr.tmpl",
        ],
    }

    @classmethod
    def import_declaration_module(cls):
        import_declaration_module()

    @classmethod
    def reload_declaration_module(cls, reload):
        import_declaration_module(reload=reload)

    def update_role(self):
        hr = self.registry.Pyramid.Role.ensure_exists(
            "hr",
            [
                {
                    "code": "role-rh-employee",
                    "model": "Model.Company.Employee",
                    "perms": PERM_WRITE,
                },
                {
                    "code": "role-rh-employee-contact",
                    "model": "Model.Company.Employee.Contact",
                    "perms": PERM_WRITE,
                },
                {
                    "code": "role-rh-employee-tag",
                    "model": "Model.Company.Employee.Tag",
                    "perms": PERM_WRITE,
                },
                {
                    "code": "role-rh-employee-contract",
                    "model": "Model.Company.Employee.Contract",
                    "perms": PERM_WRITE,
                },
            ],
            label="HR"
        )
        admin = self.registry.Pyramid.Role.ensure_exists("admin", [])
        if hr not in admin.children:
            admin.children.append(hr)

    def update(self, latest):
        self.import_file_xml("Model.FuretUI.Space", "data", "spaces.xml")
        self.import_file_xml("Model.FuretUI.Resource", "data", "resources.xml")
        self.import_file_xml("Model.FuretUI.Menu", "data", "menus.xml")
        self.update_role()
