def import_declaration_module(reload=None):
    from . import core
    if reload is not None:
        reload(core)
