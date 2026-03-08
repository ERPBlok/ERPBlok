def import_declaration_module(reload=None):
    from . import attachment
    from . import mixin

    if reload is not None:
        reload(attachment)
        reload(mixin)
