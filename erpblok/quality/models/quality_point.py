from anyblok import Declarations
from anyblok.column import Integer, String, Selection
from anyblok.relationship import Many2One


register = Declarations.register
Model = Declarations.Model
Mixin = Declarations.Mixin


@register(Model)
class QualityPoint(Mixin.AuditMixin):

    id = Integer(primary_key=True)
    name = String(nullable=False)
    product = Many2One(model='Model.Product', nullable=False)
    operation_type = Selection(selections='get_operation_types', default='reception', nullable=False)

    @classmethod
    def get_operation_types(cls):
        return {
            'reception': 'Reception',
            'delivery': 'Delivery',
            'production': 'Production',
        }
