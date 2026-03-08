from anyblok import Declarations
from anyblok.column import Integer, String, Text, Selection
from anyblok.relationship import Many2One


register = Declarations.register
Model = Declarations.Model
Mixin = Declarations.Mixin


@register(Model)
class QualityAlert(Mixin.AuditMixin):

    id = Integer(primary_key=True)
    check = Many2One(model='Model.QualityCheck', nullable=False)
    description = Text(nullable=False)
    state = Selection(selections='get_states', default='open', nullable=False)

    @classmethod
    def get_states(cls):
        return {
            'open': 'Open',
            'resolved': 'Resolved',
        }
