from anyblok import Declarations
from anyblok.column import Integer, String, Selection
from anyblok.relationship import Many2One


register = Declarations.register
Model = Declarations.Model


@register(Model)
class Journal:

    id = Integer(primary_key=True)
    code = String(nullable=False)
    name = String(nullable=False)
    type = Selection(selections='get_types', nullable=False)
    company = Many2One(model='Model.Partner.Company', nullable=False)

    @classmethod
    def get_types(cls):
        return {
            'sale': 'Sale',
            'purchase': 'Purchase',
            'cash': 'Cash',
            'bank': 'Bank',
            'general': 'General',
        }
