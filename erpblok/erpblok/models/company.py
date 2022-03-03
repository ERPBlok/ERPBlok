from anyblok import Declarations
from anyblok.column import String, Integer
from anyblok.relationship import Many2One


register = Declarations.register
Model = Declarations.Model
Mixin = Declarations.Mixin


@register(Model)
class Company:

    id = Integer(primary_key=True)
    name = String(nullable=False)


@register(Model.Company)
class Address(Mixin.ERPBlokAddress):

    company = Many2One(
        model=Model.Company, nullable=False, one2many="addresses")


@register(Model.Company)
class Contact(Mixin.ERPBlokContact):

    company = Many2One(
        model=Model.Company, nullable=False, one2many="contacts")
    address = Many2One(model=Model.Company.Address, one2many="contacts")
