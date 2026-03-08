from anyblok import Declarations
from anyblok.column import Integer, String, Password
from anyblok.relationship import Many2One


register = Declarations.register
Model = Declarations.Model
Mixin = Declarations.Mixin


@register(Model.Auth)
class Credential(Mixin.AuditMixin):

    id = Integer(primary_key=True)
    login = String(nullable=False, unique=True)
    password = Password(crypt_context={'schemes': ['pbkdf2_sha256']})
    user = Many2One(model=Model.Auth.User, nullable=False, one2many="credentials")
