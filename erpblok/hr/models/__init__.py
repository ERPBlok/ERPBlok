def import_declaration_module(reload=None):
    from . import hr
    from . import config
    if reload is not None:
        reload(hr)
        reload(config)
