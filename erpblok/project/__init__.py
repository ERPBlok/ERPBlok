from erpblok.blok import Blok
from anyblok_pyramid import PERM_WRITE
from anyblok_io.blok import BlokImporter
from .i18n import i18n


def import_declaration_module(reload=None):
    from . import models

    models.import_declaration_module(reload)


class Project(Blok, BlokImporter):
    """Helper to manage all your projects"""
    version = "0.1.0"
    author = "Jean-Sébastien Suzanne"
    category = 'Project'
    required = [
        'erpblok',
    ]

    furetui = {
        "i18n": i18n,
        "templates": [
            "templates/project.tmpl",
            "templates/task.tmpl",
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
                "code": "role-project",
                "model": "Model.ERPBlok.Project",
                "perms": PERM_WRITE,
            },
            {
                "code": "role-project-task",
                "model": "Model.ERPBlok.Project.Task",
                "perms": PERM_WRITE,
            },
        ]

    def update_role(self):
        project = self.registry.Pyramid.Role.ensure_exists(
            "project", self.project_user_role_authorizations(), label="Project"
        )
        admin = self.registry.Pyramid.Role.ensure_exists("admin", [])
        admin.children.append(project)

    def update(self, latest):
        self.import_file_xml("Model.FuretUI.Space", "data", "spaces.xml")
        self.import_file_xml("Model.FuretUI.Resource", "data", "resources.xml")
        self.import_file_xml("Model.FuretUI.Menu", "data", "menus.xml")
        self.update_role()
