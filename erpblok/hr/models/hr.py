from anyblok import Declarations
from anyblok.column import String, Integer
from anyblok.relationship import Many2One, Many2Many


register = Declarations.register
Model = Declarations.Model
Mixin = Declarations.Mixin


@register(Model.Company)
class Employee(Mixin.ERPBlokAddress, Mixin.ERPBlokCompany):

    name = String(nullable=False)
    tags = Many2Many(model="Model.Company.Employee.Tag")


@register(Model.Company.Employee)
class Contact(Mixin.ERPBlokContact):

    employee = Many2One(
        model=Model.Company.Employee, nullable=False, one2many="contacts")


@register(Model.Company.Employee)
class Tag(Mixin.ERPBlokCompany):

    id = Integer(primary_key=True)
    label = String(nullable=False)
