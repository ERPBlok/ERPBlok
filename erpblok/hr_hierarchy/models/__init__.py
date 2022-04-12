def import_declaration_module(reload=None):
    from . import hr
    if reload is not None:
        reload(hr)
