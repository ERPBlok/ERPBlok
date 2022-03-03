def import_declaration_module(reload=None):
    from . import party
    if reload is not None:
        reload(party)
