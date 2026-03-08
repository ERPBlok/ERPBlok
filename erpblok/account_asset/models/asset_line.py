from anyblok import Declarations
from anyblok.column import Integer, Float, Date
from anyblok.relationship import Many2One


register = Declarations.register
Model = Declarations.Model
Mixin = Declarations.Mixin


@register(Model)
class AssetLine(Mixin.AuditMixin):

    id = Integer(primary_key=True)
    asset = Many2One(model=Model.Asset, nullable=False, one2many="lines")
    date = Date(nullable=False)
    amount = Float(default=0.0, nullable=False)
    move = Many2One(model=Model.Account.Move)

    def create_move(self):
        """Generate accounting entry for this depreciation line
        """
        if self.move:
            raise ValueError("Accounting move already exists for this line")

        Move = self.anyblok.Model.Account.AccountMove
        Line = self.anyblok.Model.Account.AccountMoveLine
        
        move = Move.insert(
            journal=self.asset.journal,
            date=self.date,
            ref=f"Depreciation: {self.asset.name}"
        )
        
        # Debit: Depreciation Expense
        Line.insert(
            move=move,
            account=self.asset.depreciation_account,
            name=f"Depreciation: {self.asset.name}",
            debit=self.amount,
            credit=0.0
        )
        
        # Credit: Asset Account
        Line.insert(
            move=move,
            account=self.asset.category_account,
            name=f"Depreciation: {self.asset.name}",
            debit=0.0,
            credit=self.amount
        )
        
        self.move = move
        return move
