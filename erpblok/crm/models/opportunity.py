from anyblok import Declarations
from anyblok.column import Integer, String, Float, Selection
from anyblok.relationship import Many2One


register = Declarations.register
Model = Declarations.Model
Mixin = Declarations.Mixin


@register(Model)
class Opportunity(Mixin.AuditMixin):

    id = Integer(primary_key=True)
    name = String(nullable=False)
    partner = Many2One(model='Model.Partner')
    expected_revenue = Float(default=0.0)
    probability = Float(default=0.0)
    stage = Selection(selections='get_stages', default='new', nullable=False)

    @classmethod
    def get_stages(cls):
        return {
            'new': 'New',
            'qualification': 'Qualification',
            'proposition': 'Proposition',
            'won': 'Won',
            'lost': 'Lost',
        }

    def action_make_sale(self):
        Order = self.anyblok.Sale.Order
        order = Order.insert(
            partner=self.partner,
            type='standard',
            state='draft'
        )
        return order
