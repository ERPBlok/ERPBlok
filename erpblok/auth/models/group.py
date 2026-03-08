from anyblok import Declarations
from anyblok.column import Integer, String, Text
from anyblok.relationship import Many2Many


register = Declarations.register
Model = Declarations.Model
Mixin = Declarations.Mixin


@register(Model)
class Auth:
    pass


@register(Model.Auth)
class Group(Mixin.AuditMixin):

    id = Integer(primary_key=True)
    name = String(nullable=False)
    description = Text()
