def import_declaration_module(reload=None):
    from . import vehicle
    from . import odometer
    from . import fuel
    from . import invoice

    if reload is not None:
        reload(vehicle)
        reload(odometer)
        reload(fuel)
        reload(invoice)
