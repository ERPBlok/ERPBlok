from anyblok import Declarations
from anyblok.column import Integer, String, Selection
from anyblok.relationship import Many2One


register = Declarations.register
Model = Declarations.Model


@register(Model)
class Account:

    id = Integer(primary_key=True)
    code = String(nullable=False)
    name = String(nullable=False)
    type = Selection(selections='get_types', nullable=False)
    company = Many2One(model='Model.Partner.Company', nullable=False)

    @classmethod
    def get_types(cls):
        return {
            'receivable': 'Receivable',
            'payable': 'Payable',
            'liquidity': 'Liquidity',
            'income': 'Income',
            'expense': 'Expense',
            'other': 'Other',
        }
