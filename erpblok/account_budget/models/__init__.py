def import_declaration_module(reload=None):
    from . import budget
    from . import budget_line

    if reload is not None:
        reload(budget)
        reload(budget_line)
