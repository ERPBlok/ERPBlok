def import_declaration_module(reload=None):
    from . import product
    from . import warehouse
    from . import location
    from . import move

    if reload is not None:
        reload(product)
        reload(warehouse)
        reload(location)
        reload(move)
