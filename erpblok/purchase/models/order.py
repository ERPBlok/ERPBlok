from anyblok import Declarations
from anyblok.column import Integer, String, Selection, Date
from anyblok.relationship import Many2One


register = Declarations.register
Model = Declarations.Model


@register(Model)
class PurchaseOrder:

    id = Integer(primary_key=True)
    name = String(nullable=False)
    partner = Many2One(model='Model.Partner', nullable=False)
    date = Date(nullable=False)
    state = Selection(selections='get_states', default='draft', nullable=False)

    @classmethod
    def get_states(cls):
        return {
            'draft': 'Draft',
            'confirmed': 'Confirmed',
            'done': 'Done',
            'cancelled': 'Cancelled',
        }

    def action_confirm(self):
        if self.state == 'draft':
            self.state = 'confirmed'
            for line in self.lines:
                if not line.price_unit:
                    line.price_unit = line.product.get_purchase_price(line.qty, self.partner)
