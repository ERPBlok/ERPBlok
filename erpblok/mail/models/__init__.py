def import_declaration_module(reload=None):
    from . import message
    from . import follower
    from . import notification
    from . import mixin

    if reload is not None:
        reload(message)
        reload(follower)
        reload(notification)
        reload(mixin)
