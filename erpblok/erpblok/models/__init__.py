def import_declaration_module(reload=None):
    from . import core
    from . import mixins
    if reload is not None:
        reload(core)
        reload(mixins)
