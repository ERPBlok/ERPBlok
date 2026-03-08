from anyblok import Declarations
from anyblok.column import Integer, String, Float, Selection, Date
from anyblok.relationship import Many2One, One2Many
from datetime import date, timedelta


register = Declarations.register
Model = Declarations.Model
Mixin = Declarations.Mixin


@register(Model)
class Asset(Mixin.AuditMixin):

    id = Integer(primary_key=True)
    name = String(nullable=False)
    purchase_value = Float(default=0.0, nullable=False)
    salvage_value = Float(default=0.0)
    method = Selection(selections='get_methods', default='linear', nullable=False)
    duration = Integer(default=5, nullable=False)  # years
    date = Date(default=date.today, nullable=False)
    
    # Accounting configuration
    category_account = Many2One(model=Model.Account, nullable=False)
    depreciation_account = Many2One(model=Model.Account, nullable=False)
    journal = Many2One(model=Model.Account, nullable=False)

    @classmethod
    def get_methods(cls):
        return {
            'linear': 'Linear',
            'degressive': 'Degressive',
        }

    def compute_board(self):
        """Compute depreciation board
        """
        for line in self.lines:
            line.delete()

        depreciable_value = self.purchase_value - self.salvage_value
        if self.duration <= 0:
            return

        if self.method == 'linear':
            annual_depreciation = depreciable_value / self.duration
            for i in range(1, self.duration + 1):
                self.anyblok.Model.AssetLine.insert(
                    asset=self,
                    date=self.date + timedelta(days=365 * i),
                    amount=annual_depreciation
                )
        elif self.method == 'degressive':
            # Simplified degressive for demonstration
            remaining_value = depreciable_value
            rate = 2.0 / self.duration  # Declining balance 200%
            for i in range(1, self.duration + 1):
                amount = remaining_value * rate
                if i == self.duration:
                    amount = remaining_value  # Last year takes all remaining
                
                self.anyblok.Model.AssetLine.insert(
                    asset=self,
                    date=self.date + timedelta(days=365 * i),
                    amount=amount
                )
                remaining_value -= amount
