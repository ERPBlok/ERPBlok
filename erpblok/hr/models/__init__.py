def import_declaration_module(reload=None):
    from . import department
    from . import contract

    if reload is not None:
        reload(department)
        reload(contract)
