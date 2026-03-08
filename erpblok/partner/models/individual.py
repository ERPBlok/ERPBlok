from anyblok import Declarations
from anyblok.column import Integer, String


register = Declarations.register
Model = Declarations.Model


@register(Model.Partner)
class Individual:

    id = Integer(primary_key=True, foreign_key=Model.Partner.use("id"))
    firstname = String()
    lastname = String()
    gender = String()

    def get_display_name(self):
        return f"{self.lastname} {self.firstname}".strip() or self.name
