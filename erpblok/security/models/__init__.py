def import_declaration_module(reload=None):
    from . import access_right
    from . import access_rule
    from . import logic

    if reload is not None:
        reload(access_right)
        reload(access_rule)
        reload(logic)
