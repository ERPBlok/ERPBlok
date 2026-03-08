from anyblok import Declarations
from anyblok.column import Integer, String
from anyblok.relationship import Many2One


register = Declarations.register
Model = Declarations.Model


@register(Model)
class Project:

    id = Integer(primary_key=True)
    name = String(nullable=False)
    partner = Many2One(model='Model.Partner')
