def import_declaration_module(reload=None):
    from . import equipment
    from . import team
    from . import request

    if reload is not None:
        reload(equipment)
        reload(team)
        reload(request)
