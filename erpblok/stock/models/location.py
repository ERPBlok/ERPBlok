from anyblok import Declarations
from anyblok.column import Integer, String
from anyblok.relationship import Many2One


register = Declarations.register
Model = Declarations.Model


@register(Model.Stock)
class Location:

    id = Integer(primary_key=True)
    name = String(nullable=False)
    parent = Many2One(model='Model.Stock.Location', one2many='children')
    warehouse = Many2One(model=Model.Stock.Warehouse, one2many='locations')
