def import_declaration_module(reload=None):
    from . import group
    from . import user
    from . import credential

    if reload is not None:
        reload(group)
        reload(user)
        reload(credential)
