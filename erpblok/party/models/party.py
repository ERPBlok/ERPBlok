from anyblok import Declarations
from anyblok.column import String, Integer
from anyblok.relationship import Many2One, Many2Many
from anyblok_pyramid.bloks.pyramid.restrict import restrict_query_by_user
from anyblok_furetui.field import Contextual
from anyblok_furetui.factory import (
    SingletonModelFactory, ContextualModelFactory)


register = Declarations.register
Model = Declarations.Model
Mixin = Declarations.Mixin


@register(Model, factory=ContextualModelFactory)
class Party:

    id = Integer(primary_key=True)
    name = String(nullable=False)
    companies = Many2Many(model='Model.Company')
    code = Contextual(String(nullable=False), identity='company')

    @restrict_query_by_user()
    def restrict_by_companies(cls, query, user):
        return user.restrict_by_companies(query, cls.companies)

    @classmethod
    def define_contextual_models(cls):
        return {
            'company': {
                'model': cls.anyblok.Company,
            }
        }

    def insert_code(self):
        for company in self.companies:
            with self.context.set(company=company):
                if self.code is None:
                    seq = self.Configuration.get().sequence
                    self.code = seq.nextval()

    @classmethod
    def furetui_insert(cls, **kw):
        res = super().furetui_insert(**kw)
        cls.precommit_hook('insert_code', res)
        return res

    def furetui_update(self, **kw):
        res = super().furetui_update(**kw)
        self.precommit_hook('insert_code', self)
        return res


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


@register(Model.System)
class Sequence:

    @classmethod
    def get_types(cls):
        res = super().get_types()
        res['Model.Party.Sequence'] = 'Party'
        return res


@register(Model.Party, tablename=Model.System.Sequence)
class Sequence(Model.System.Sequence):  # noqa
    pass

    @restrict_query_by_user()
    def restrict_by_company(cls, query, user):
        return user.restrict_by_company(query, cls.company)


@register(Model.Party, factory=SingletonModelFactory)
class Configuration:

    sequence = Contextual(
        Many2One(model=Model.Party.Sequence, nullable=False),
        identity='company')

    @classmethod
    def define_contextual_models(cls):
        return {
            'company': {
                'model': cls.anyblok.Company,
            }
        }
