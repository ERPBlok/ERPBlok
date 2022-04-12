from anyblok import Declarations
from anyblok.column import String, Text, Integer
from anyblok.relationship import Many2One


register = Declarations.register
Model = Declarations.Model
Mixin = Declarations.Mixin


@register(Model.Company)
class Employee:

    supervisor = Many2One(
        model='Model.Company.Employee',
        one2many='subordinates')
    team = Many2One(
        model='Model.Company.Employee.Team',
        one2many='employees')


@register(Model.Company.Employee)
class Team(Mixin.ERPBlokCompany):

    id = Integer(primary_key=True)
    label = String(nullable=False)
    description = Text()
