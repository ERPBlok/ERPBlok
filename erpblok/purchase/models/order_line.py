from anyblok import Declarations
from anyblok.column import Integer, Float
from anyblok.relationship import Many2One


register = Declarations.register
Model = Declarations.Model


@register(Model)
class PurchaseOrderLine:

    id = Integer(primary_key=True)
    order = Many2One(model='Model.PurchaseOrder', nullable=False, one2many='lines')
    product = Many2One(model='Model.Product', nullable=False)
    qty = Float(default=1.0, nullable=False)
    price_unit = Float(default=0.0)

    @property
    def price_subtotal(self):
        return self.qty * self.price_unit
