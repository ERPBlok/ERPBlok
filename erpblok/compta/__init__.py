from erpblok.blok import Blok
from anyblok_pyramid import PERM_WRITE
from anyblok_io.blok import BlokImporter
from .i18n import i18n


def import_declaration_module(reload=None):
    from . import models

    models.import_declaration_module(reload)


class Compta(Blok, BlokImporter):
    """Helper to manage all your projects"""
    version = "0.1.0"
    author = "Jean-Sébastien Suzanne"
    category = 'Account'
    required = [
        'erpblok',
        'anyblok-mixins',
    ]

    furetui = {
        "i18n": i18n,
        "templates": [
            "templates/account.tmpl",
            "templates/journal.tmpl",
        ],
    }

    @classmethod
    def import_declaration_module(cls):
        import_declaration_module()

    @classmethod
    def reload_declaration_module(cls, reload):
        import_declaration_module(reload=reload)

    def project_user_role_authorizations(self):
        return [
            {
                "code": "role-account",
                "model": "Model.ERPBlok.Account",
                "perms": PERM_WRITE,
            },
            {
                "code": "role-account-journal",
                "model": "Model.ERPBlok.Account.Journal",
                "perms": PERM_WRITE,
            },
        ]

    def update_role(self):
        account = self.registry.Pyramid.Role.ensure_exists(
            "account", self.project_user_role_authorizations(), label="Account"
        )
        admin = self.registry.Pyramid.Role.ensure_exists("admin", [])
        if account not in admin.children:
            admin.children.append(account)

    def update(self, latest):
        self.import_file_xml("Model.FuretUI.Space", "data", "spaces.xml")
        self.import_file_xml("Model.FuretUI.Resource", "data", "resources.xml")
        self.import_file_xml("Model.FuretUI.Menu", "data", "menus.xml")
        self.update_role()

    def update_demo(self, latest):
        self.import_file_xml("Model.ERPBlok.Account", "demo", "accounts.xml")
        self.import_file_xml("Model.ERPBlok.Account.Journal", "demo",
                             "journals.xml")

        Account = self.registry.ERPBlok.Account
        Journal = Account.Journal
        Move = Account.Move
        Header = Move.Header

        header = Header.insert(
            reference='facture 1',
            journal=Journal.query().get('BANK')
        )
        Move.insert(header=header, account=Account.query().get('507'),
                    credit=200),
        Move.insert(header=header, account=Account.query().get('401001'),
                    credit=1000),
