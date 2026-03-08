def import_declaration_module(reload=None):
    from . import product
    from . import service

    if reload is not None:
        reload(product)
        reload(service)
