from anyblok import Declarations
from anyblok.column import Integer, Float
from anyblok.relationship import Many2One


register = Declarations.register
Model = Declarations.Model


@register(Model.Account.Move)
class Line:

    id = Integer(primary_key=True)
    move = Many2One(model=Model.Account.Move, nullable=False, one2many='lines')
    account = Many2One(model=Model.Account, nullable=False)
    partner = Many2One(model=Model.Partner)
    debit = Float(default=0.0)
    credit = Float(default=0.0)
