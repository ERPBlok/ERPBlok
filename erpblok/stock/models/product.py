from anyblok import Declarations
from anyblok.column import Integer


register = Declarations.register
Model = Declarations.Model


@register(Model.Product)
class StorableProduct:

    id = Integer(primary_key=True, foreign_key=Model.Product.use("id"))

    def is_storable(self):
        return True

    @property
    def qty_available(self):
        qty = 0
        for move in self.incoming_moves:
            qty += move.qty
        for move in self.outgoing_moves:
            qty -= move.qty
        return qty
