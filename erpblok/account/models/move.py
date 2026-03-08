from anyblok import Declarations
from anyblok.column import Integer, String, Date
from anyblok.relationship import Many2One


register = Declarations.register
Model = Declarations.Model


@register(Model.Account)
class Move:

    id = Integer(primary_key=True)
    name = String(nullable=False)
    date = Date(nullable=False)
    journal = Many2One(model=Model.Journal, nullable=False)
    company = Many2One(model=Model.Partner.Company, nullable=False)
    currency = Many2One(model=Model.Account.Currency, nullable=False)
