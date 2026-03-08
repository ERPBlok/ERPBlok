from anyblok import Declarations
from anyblok.column import Integer, String, DateTime
from anyblok.relationship import Many2One
from datetime import datetime


register = Declarations.register
Model = Declarations.Model


@register(Model)
class BarcodeScan:

    id = Integer(primary_key=True)
    barcode = String(nullable=False)
    timestamp = DateTime(default=datetime.now, nullable=False)
    operator = Many2One(model='Model.Partner')
