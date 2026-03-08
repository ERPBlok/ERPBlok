def import_declaration_module(reload=None):
    from . import order

    if reload is not None:
        reload(order)
