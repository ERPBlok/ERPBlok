def import_declaration_module(reload=None):
    from . import account
    from . import journal
    from . import currency
    from . import move
    from . import move_line

    if reload is not None:
        reload(account)
        reload(journal)
        reload(currency)
        reload(move)
        reload(move_line)
