from anyblok import Declarations
from anyblok.column import Integer, Float, Date
from anyblok.relationship import Many2One
from datetime import date


register = Declarations.register
Model = Declarations.Model


@register(Model)
class VehicleLogFuel:

    id = Integer(primary_key=True)
    vehicle = Many2One(model='Model.Vehicle', nullable=False)
    liter = Float(default=0.0)
    amount = Float(default=0.0, nullable=False)
    date = Date(default=date.today, nullable=False)
