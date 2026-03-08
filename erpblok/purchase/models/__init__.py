def import_declaration_module(reload=None):
    from . import order
    from . import order_line

    if reload is not None:
        reload(order)
        reload(order_line)
