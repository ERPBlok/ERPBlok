def import_declaration_module(reload=None):
    from . import system_blok

    if reload is not None:
        reload(system_blok)
