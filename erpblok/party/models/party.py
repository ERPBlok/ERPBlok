from anyblok import Declarations
from anyblok.column import String, Integer
from anyblok.relationship import Many2One


register = Declarations.register
Model = Declarations.Model
Mixin = Declarations.Mixin


@register(Model)
class Party:

    id = Integer(primary_key=True)
    name = String(nullable=False)


@register(Model.Party)
class Address(Mixin.ERPBlokAddress):

    party = Many2One(
        model=Model.Party, nullable=False, one2many="addresses")


@register(Model.Party)
class Contact(Mixin.ERPBlokContact):

    party = Many2One(
        model=Model.Party, nullable=False, one2many="contacts")
    address = Many2One(model=Model.Party.Address, one2many="contacts")
