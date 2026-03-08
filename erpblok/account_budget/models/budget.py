from anyblok import Declarations
from anyblok.column import Integer, String, Date
from anyblok.relationship import One2Many


register = Declarations.register
Model = Declarations.Model
Mixin = Declarations.Mixin


@register(Model)
class Budget(Mixin.AuditMixin):

    id = Integer(primary_key=True)
    name = String(nullable=False)
    date_from = Date(nullable=False)
    date_to = Date(nullable=False)