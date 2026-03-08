from anyblok import Declarations
from anyblok.column import String


register = Declarations.register
Model = Declarations.Model


@register(Model.Stock)
class Location:

    barcode = String()
