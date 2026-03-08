from anyblok import Declarations
from anyblok.column import Integer, Float, Date
from anyblok.relationship import Many2One


register = Declarations.register
Model = Declarations.Model


@register(Model)
class TimesheetLine:

    id = Integer(primary_key=True)
    employee = Many2One(model='Model.Partner.Individual.Employee', nullable=False)
    task = Many2One(model='Model.Project.Task', nullable=False)
    date = Date(nullable=False)
    duration = Float(default=0.0, nullable=False)
