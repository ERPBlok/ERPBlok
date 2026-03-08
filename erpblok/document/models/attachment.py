from anyblok import Declarations
from anyblok.column import Integer, String, LargeBinary


register = Declarations.register
Model = Declarations.Model


@register(Model)
class Attachment:

    id = Integer(primary_key=True)
    res_model = String(nullable=False)
    res_id = Integer(nullable=False)
    file_data = LargeBinary()
    mimetype = String()
