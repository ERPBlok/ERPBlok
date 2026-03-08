from anyblok import Declarations
from anyblok.column import Integer, Float, Selection
from anyblok.relationship import Many2One


register = Declarations.register
Model = Declarations.Model
Mixin = Declarations.Mixin


@register(Model)
class ProductionOrder(Mixin.AuditMixin):

    id = Integer(primary_key=True)
    product = Many2One(model='Model.Product', nullable=False)
    qty = Float(default=1.0, nullable=False)
    bom = Many2One(model='Model.BOM', nullable=False)
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

    def action_done(self):
        if self.state != 'confirmed':
            return

        Move = self.anyblok.Model.Stock.Move
        
        # 1. Consume components
        for line in self.bom.lines:
            Move.insert(
                product=line.product,
                qty=line.qty * self.qty,
                type='outgoing',  # Consumed from stock
            )
            
        # 2. Produce finished good
        Move.insert(
            product=self.product,
            qty=self.qty,
            type='incoming',  # Added to stock
        )

        self.state = 'done'
