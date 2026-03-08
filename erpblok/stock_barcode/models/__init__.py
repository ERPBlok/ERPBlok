def import_declaration_module(reload=None):
    from . import product
    from . import location
    from . import barcode_scan

    if reload is not None:
        reload(product)
        reload(location)
        reload(barcode_scan)
