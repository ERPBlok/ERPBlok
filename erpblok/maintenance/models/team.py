from anyblok import Declarations
from anyblok.column import Integer, String
from anyblok.relationship import Many2Many


register = Declarations.register
Model = Declarations.Model
Mixin = Declarations.Mixin


@register(Model)
class MaintenanceTeam(Mixin.AuditMixin):

    id = Integer(primary_key=True)
    name = String(nullable=False)
    members = Many2Many(model='Model.Partner.Individual.Employee')
