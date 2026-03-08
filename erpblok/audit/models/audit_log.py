from anyblok import Declarations
from anyblok.column import Integer, String, DateTime, Text


register = Declarations.register
Model = Declarations.Model


@register(Model)
class AuditLog:

    id = Integer(primary_key=True)
    model_name = String(nullable=False)
    res_id = Integer(nullable=False)
    user_id = Integer()  # Simplified, could be a Many2One to User
    change_date = DateTime(nullable=False)
    old_value = Text()
    new_value = Text()
