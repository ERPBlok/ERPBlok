def import_declaration_module(reload=None):
    from . import audit_log
    from . import mixin

    if reload is not None:
        reload(audit_log)
        reload(mixin)
