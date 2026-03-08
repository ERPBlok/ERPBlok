from anyblok import Declarations
from anyblok.column import String


register = Declarations.register
Model = Declarations.Model


@register(Model)
class Product:

    barcode = String()
