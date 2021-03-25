def import_declaration_module(reload=None):
    from . import account
    from . import journal
    from . import move
    if reload is not None:
        reload(account)
        reload(journal)
        reload(move)
