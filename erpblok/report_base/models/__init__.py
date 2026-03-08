def import_declaration_module(reload=None):
    from . import report_definition
    # from . import sales_analysis

    if reload is not None:
        reload(report_definition)
        # reload(sales_analysis)
