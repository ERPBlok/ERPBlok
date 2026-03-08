def import_declaration_module(reload=None):
    from . import lead
    from . import opportunity

    if reload is not None:
        reload(lead)
        reload(opportunity)
