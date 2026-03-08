from anyblok import Declarations
from anyblok.column import Integer, Boolean
from anyblok.relationship import Many2One


register = Declarations.register
Model = Declarations.Model


@register(Model)
class Notification:

    id = Integer(primary_key=True)
    message = Many2One(model='Model.Message', nullable=False)
    partner = Many2One(model='Model.Partner', nullable=False)
    is_read = Boolean(default=False)
