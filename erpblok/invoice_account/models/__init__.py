def import_declaration_module(reload=None):
    from . import invoice

    if reload is not None:
        reload(invoice)
