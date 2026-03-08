from anyblok import Declarations
from anyblok.column import Integer, String, Float, Boolean, Selection
from anyblok.relationship import Many2One


register = Declarations.register
Model = Declarations.Model


@register(Model)
class Tax:

    id = Integer(primary_key=True)
    name = String(nullable=False)
    amount = Float(default=0.0, nullable=False)
    type = Selection(selections='get_types', default='percent', nullable=False)
    price_include = Boolean(default=False)
    tax_group = Many2One(model='Model.TaxGroup', one2many="taxes")

    @classmethod
    def get_types(cls):
        return {
            'percent': 'Percentage',
            'fixed': 'Fixed Amount',
        }

    def compute_all(self, price, qty=1.0):
        if self.type == 'percent':
            if self.price_include:
                tax_amount = price - (price / (1 + self.amount / 100))
                base_amount = price - tax_amount
            else:
                tax_amount = price * (self.amount / 100)
                base_amount = price
        elif self.type == 'fixed':
            tax_amount = self.amount * qty
            base_amount = price
        else:
            tax_amount = 0.0
            base_amount = price

        return {
            'tax_amount': tax_amount,
            'total_amount': base_amount + tax_amount if not self.price_include else price,
            'base_amount': base_amount,
        }
