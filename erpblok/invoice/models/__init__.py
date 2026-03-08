def import_declaration_module(reload=None):
    from . import invoice
    from . import invoice_line

    if reload is not None:
        reload(invoice)
        reload(invoice_line)
