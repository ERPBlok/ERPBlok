def import_declaration_module(reload=None):
    from . import timesheet_line

    if reload is not None:
        reload(timesheet_line)
