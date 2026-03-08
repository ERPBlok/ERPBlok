from anyblok.declarations import Declarations
from sqlalchemy import inspect


register = Declarations.register
Mixin = Declarations.Mixin


@register(Mixin)
class AuditMixin:

    @classmethod
    def before_update_orm_event(cls, mapper, connection, target):
        inspected = inspect(target)
        audit_log_obj = target.anyblok.Model.AuditLog
        now = target.anyblok.anyblok_datetime.now()
        
        for attr in inspected.mapper.column_attrs:
            hist = inspected.get_history(attr.key, True)
            if hist.has_changes():
                old_value = str(hist.deleted[0]) if hist.deleted else None
                new_value = str(hist.added[0]) if hist.added else None
                
                audit_log_obj.insert(
                    model_name=target.__registry_name__,
                    res_id=target.id,
                    # user_id should be retrieved from session/context if available
                    change_date=now,
                    old_value=old_value,
                    new_value=new_value,
                )
