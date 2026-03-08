from anyblok import Declarations
from anyblok.column import Integer, Float
from anyblok.relationship import Many2One


register = Declarations.register
Model = Declarations.Model


@register(Model.Stock)
class Move:

    id = Integer(primary_key=True)
    product = Many2One(model=Model.Product.StorableProduct, nullable=False, one2many='moves')
    qty = Float(nullable=False)
    source_location = Many2One(model=Model.Stock.Location, nullable=False, one2many='outgoing_moves')
    dest_location = Many2One(model=Model.Stock.Location, nullable=False, one2many='incoming_moves')
