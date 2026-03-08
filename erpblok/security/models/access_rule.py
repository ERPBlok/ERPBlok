from anyblok import Declarations
from anyblok.column import Integer, String, Text
from anyblok.relationship import Many2One


register = Declarations.register
Model = Declarations.Model
Mixin = Declarations.Mixin


@register(Model.Security.Access)
class Rule(Mixin.AuditMixin):

    id = Integer(primary_key=True)
    group = Many2One(model=Model.Auth.Group, nullable=False, one2many="access_rules")
    model_name = String(nullable=False)
    domain_force = Text(nullable=False)
