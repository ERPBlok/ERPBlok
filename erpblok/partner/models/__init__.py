def import_declaration_module(reload=None):
    from . import partner
    from . import company
    from . import individual
    from . import employee

    if reload is not None:
        reload(partner)
        reload(company)
        reload(individual)
        reload(employee)
