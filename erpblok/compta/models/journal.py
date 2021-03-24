from anyblok.declarations import Declarations
from anyblok.column import String, Text, Selection


@Declarations.register(Declarations.Model.ERPBlok.Account)
class Journal:

    code = String(primary_key=True, size=20)
    label = String(nullable=False)
    description = Text()
    type = Selection(selections={
        'customer_invoice': 'Customer invoice',
        'customer_refund': 'Customer refund',
        'supplier_invoice': 'Supplier invoice',
        'supplier_refund': 'Supplier refund',
    }, default='customer_invoice')
