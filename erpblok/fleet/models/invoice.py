from anyblok import Declarations
from anyblok.relationship import Many2One


register = Declarations.register
Model = Declarations.Model


@register(Model.Invoice)
class Line:

    vehicle = Many2One(model=Model.Vehicle)
