from anyblok import Declarations
from anyblok.column import Integer, String


register = Declarations.register
Model = Declarations.Model


@register(Model.Sale.Order)
class WebOrder:

    id = Integer(primary_key=True, foreign_key=Model.Sale.Order.use("id"))
    cart_token = String()
    gateway_ref = String()
