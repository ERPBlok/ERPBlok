def import_declaration_module(reload=None):
    from . import project
    from . import task
    if reload is not None:
        reload(project)
        reload(task)
