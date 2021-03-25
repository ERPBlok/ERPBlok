from anyblok.declarations import Declarations
from anyblok.column import String, Integer, Decimal
from anyblok.relationship import Many2One

Model = Declarations.Model
Mixin = Declarations.Mixin


@Declarations.register(Model.ERPBlok.Account)
class Move:

    id = Integer(primary_key=True)
    label = String()
    account = Many2One(model=Model.ERPBlok.Account,
                       nullable=False)
    # header n'utilise pas la declaration car elle
    # n'existe pas encore
    header = Many2One(model='Model.ERPBlok.Account.Move.Header',
                      nullable=False, one2many="moves")
    credit = Decimal(default=0)
    debit = Decimal(default=0)

    def get_balance(self):
        return self.credit - self.debit


# TrackModel => Ajoute create_date edit_date (auto)
@Declarations.register(Model.ERPBlok.Account.Move)
class Header(Mixin.TrackModel):
    id = Integer(primary_key=True)
    reference = String(nullable=False)
    journal = Many2One(model=Model.ERPBlok.Account.Journal,
                       nullable=False)

    def get_amount(self):
        return sum([
            move.get_balance()
            for move in self.moves
        ])
