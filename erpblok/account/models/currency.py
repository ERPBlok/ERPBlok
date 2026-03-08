from anyblok import Declarations
from anyblok.column import Integer, String


register = Declarations.register
Model = Declarations.Model


@register(Model.Account)
class Currency:

    id = Integer(primary_key=True)
    code = String(nullable=False)
    name = String(nullable=False)
    symbol = String(nullable=False)
