from anyblok import Declarations
from anyblok.column import Integer, Boolean
from anyblok.relationship import Many2One, Many2Many


register = Declarations.register
Model = Declarations.Model


@register(Model.Auth)
class User(Model.Partner):

    id = Integer(primary_key=True, foreign_key=Model.Partner.use("id"))
    active = Boolean(default=True)
    
    company_id = Many2One(model=Model.Partner.Company)
    allowed_company_ids = Many2Many(model=Model.Partner.Company)
    groups = Many2Many(model=Model.Auth.Group, many2many="users")

    @property
    def is_admin(self):
        return any(g.name == 'Admins' for g in self.groups)

    def check_password(self, password):
        """Helper to check password against any linked credential
        """
        for credential in self.credentials:
            if credential.password == password:
                return True
        return False
