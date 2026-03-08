from anyblok import Declarations
from anyblok.column import Integer, Float, Selection
from anyblok.relationship import Many2One


register = Declarations.register
Model = Declarations.Model
Mixin = Declarations.Mixin


@register(Model)
class MaintenanceRequest(Mixin.AuditMixin):

    id = Integer(primary_key=True)
    equipment = Many2One(model='Model.Equipment', nullable=False)
    team = Many2One(model='Model.MaintenanceTeam')
    priority = Selection(selections='get_priorities', default='normal', nullable=False)
    maintenance_type = Selection(selections='get_types', default='corrective', nullable=False)
    duration = Float(default=0.0)  # In hours

    @classmethod
    def get_priorities(cls):
        return {
            'low': 'Low',
            'normal': 'Normal',
            'high': 'High',
        }

    @classmethod
    def get_types(cls):
        return {
            'corrective': 'Corrective',
            'preventive': 'Preventive',
        }

    @classmethod
    def generate_preventive(cls, equipment):
        """Logic to manually trigger a preventive request
        """
        return cls.insert(
            equipment=equipment,
            maintenance_type='preventive',
            priority='normal'
        )
