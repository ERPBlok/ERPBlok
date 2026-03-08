def import_declaration_module(reload=None):
    from . import quality_point
    from . import quality_check
    from . import quality_alert
    from . import stock_move

    if reload is not None:
        reload(quality_point)
        reload(quality_check)
        reload(quality_alert)
        reload(stock_move)
