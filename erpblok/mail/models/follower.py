from anyblok import Declarations
from anyblok.column import Integer, String
from anyblok.relationship import Many2One


register = Declarations.register
Model = Declarations.Model


@register(Model)
class Follower:

    id = Integer(primary_key=True)
    res_model = String(nullable=False)
    res_id = Integer(nullable=False)
    partner = Many2One(model='Model.Partner', nullable=False)
