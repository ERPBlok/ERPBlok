from anyblok import Declarations
from anyblok.column import Integer


register = Declarations.register
Model = Declarations.Model


@register(Model.Product)
class Service:

    id = Integer(primary_key=True, foreign_key=Model.Product.use("id"))
