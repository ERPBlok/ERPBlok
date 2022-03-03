from anyblok import Declarations
from anyblok.column import String, Integer
from anyblok.relationship import Many2One, Many2Many
from anyblok_pyramid.bloks.pyramid.restrict import restrict_query_by_user


register = Declarations.register
Model = Declarations.Model
Mixin = Declarations.Mixin


@register(Model)
class Party:

    id = Integer(primary_key=True)
    name = String(nullable=False)
    companies = Many2Many(model='Model.Company')

    @restrict_query_by_user()
    def restrict_by_companies(cls, query, user):
        return user.restrict_by_companies(query, cls.companies)


@register(Model.Party)
class Address(Mixin.ERPBlokAddress):

    party = Many2One(
        model=Model.Party, nullable=False, one2many="addresses")

    @restrict_query_by_user()
    def restrict_by_companies(cls, query, user):
        return user.restrict_by_companies(
            query.join(cls.party),
            cls.anyblok.Party.companies)


@register(Model.Party)
class Contact(Mixin.ERPBlokContact):

    party = Many2One(
        model=Model.Party, nullable=False, one2many="contacts")
    address = Many2One(model=Model.Party.Address, one2many="contacts")
