def import_declaration_module(reload=None):
    from . import bom
    from . import production_order

    if reload is not None:
        reload(bom)
        reload(production_order)
