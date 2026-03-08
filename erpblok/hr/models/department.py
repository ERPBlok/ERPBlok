from anyblok import Declarations
from anyblok.column import Integer, String
from anyblok.relationship import Many2One


register = Declarations.register
Model = Declarations.Model


@register(Model)
class Department:

    id = Integer(primary_key=True)
    name = String(nullable=False)
    parent = Many2One(model='Model.Department', one2many='children')
