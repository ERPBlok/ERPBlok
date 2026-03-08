from anyblok import Declarations
from anyblok.column import Integer, String


register = Declarations.register
Model = Declarations.Model


@register(Model.Partner)
class Company:

    id = Integer(primary_key=True, foreign_key=Model.Partner.use("id"))
    siret = String()
    vat_number = String()
    website = String()

    def get_display_name(self):
        return self.name
