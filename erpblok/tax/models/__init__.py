def import_declaration_module(reload=None):
    from . import tax
    from . import tax_group

    if reload is not None:
        reload(tax)
        reload(tax_group)
