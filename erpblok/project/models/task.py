from anyblok import Declarations
from anyblok.column import Integer, String
from anyblok.relationship import Many2One


register = Declarations.register
Model = Declarations.Model


@register(Model.Project)
class Task:

    id = Integer(primary_key=True)
    name = String(nullable=False)
    project = Many2One(model='Model.Project', nullable=False, one2many='tasks')
