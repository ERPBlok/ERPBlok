from anyblok import Declarations
from anyblok.column import Integer, String


register = Declarations.register
Model = Declarations.Model


@register(Model)
class Stock:
    pass


@register(Model.Stock)
class Warehouse:

    id = Integer(primary_key=True)
    name = String(nullable=False)
