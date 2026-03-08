from anyblok import Declarations
from anyblok.column import Integer, Float
from anyblok.relationship import Many2One


register = Declarations.register
Model = Declarations.Model


@register(Model.Invoice)
class Line:

    id = Integer(primary_key=True)
    invoice = Many2One(model=Model.Invoice, nullable=False, one2many='lines')
    product = Many2One(model=Model.Product)
    qty = Float(default=1.0, nullable=False)
    price_unit = Float(default=0.0)
    account = Many2One(model=Model.Account)
