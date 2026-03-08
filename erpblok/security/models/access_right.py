from anyblok import Declarations
from anyblok.column import Integer, String, Boolean
from anyblok.relationship import Many2One


register = Declarations.register
Model = Declarations.Model
Mixin = Declarations.Mixin


@register(Model)
class Security:
    pass


@register(Model.Security)
class Access:
    pass


@register(Model.Security.Access)
class Right(Mixin.AuditMixin):

    id = Integer(primary_key=True)
    group = Many2One(model=Model.Auth.Group, nullable=False, one2many="access_rights")
    model_name = String(nullable=False)
    perm_read = Boolean(default=True)
    perm_write = Boolean(default=False)
    perm_create = Boolean(default=False)
    perm_unlink = Boolean(default=False)
