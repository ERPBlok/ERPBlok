def import_declaration_module(reload=None):
    from . import asset
    from . import asset_line

    if reload is not None:
        reload(asset)
        reload(asset_line)
