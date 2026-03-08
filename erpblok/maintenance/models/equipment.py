from anyblok import Declarations
from anyblok.column import Integer, String, Date
from anyblok.relationship import Many2One


register = Declarations.register
Model = Declarations.Model
Mixin = Declarations.Mixin


@register(Model)
class Equipment(Mixin.AuditMixin):

    id = Integer(primary_key=True)
    name = String(nullable=False)
    serial_number = String()
    partner = Many2One(model='Model.Partner')
    assignation_date = Date()
    maintenance_interval = Integer(default=0)  # In months
