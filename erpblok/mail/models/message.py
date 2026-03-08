from anyblok import Declarations
from anyblok.column import Integer, String, Text
from anyblok.relationship import Many2One


register = Declarations.register
Model = Declarations.Model


@register(Model)
class Message:

    id = Integer(primary_key=True)
    res_model = String(nullable=False)
    res_id = Integer(nullable=False)
    body = Text(nullable=False)
    author = Many2One(model='Model.Partner')
