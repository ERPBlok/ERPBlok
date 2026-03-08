from anyblok import Declarations
from anyblok.column import Integer, String
from anyblok.relationship import One2Many


register = Declarations.register
Model = Declarations.Model


@register(Model)
class TaxGroup:

    id = Integer(primary_key=True)
    name = String(nullable=False)
