def import_declaration_module(reload=None):
    from . import core
    from . import mixins
    from . import company
    from . import user
    if reload is not None:
        reload(core)
        reload(mixins)
        reload(company)
        reload(user)
