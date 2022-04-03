from anyblok import Declarations
from anyblok.column import String, Integer
from anyblok.relationship import Many2One
from anyblok_pyramid_rest_api.adapter import Adapter


register = Declarations.register
Model = Declarations.Model
Mixin = Declarations.Mixin


@register(Model)
class Company:

    id = Integer(primary_key=True)
    name = String(nullable=False)

    class FuretUIAdapter(Adapter):

        @Adapter.tag('user-access')
        def tag_is_an_alley(self, querystring, query):
            Company = self.registry.Company
            user = Company.context['user']
            query = query.filter(
                Company.name.in_([
                    useraccess.company.name
                    for useraccess in user.companies_accesses]))
            return query


@register(Model.Company)
class Address(Mixin.ERPBlokAddress):

    company = Many2One(
        model=Model.Company, nullable=False, one2many="addresses")


@register(Model.Company)
class Contact(Mixin.ERPBlokContact):

    company = Many2One(
        model=Model.Company, nullable=False, one2many="contacts")
    address = Many2One(model=Model.Company.Address, one2many="contacts")
