from anyblok import Declarations
from anyblok.column import Integer, String, Text


register = Declarations.register
Model = Declarations.Model
Mixin = Declarations.Mixin


@register(Model)
class Lead(Mixin.AuditMixin):

    id = Integer(primary_key=True)
    name = String(nullable=False)
    contact_name = String()
    email = String()
    phone = String()
    description = Text()

    def convert_to_partner(self, type='individual'):
        if type == 'individual':
            Model = self.anyblok.Partner.Individual
        else:
            Model = self.anyblok.Partner.Company

        partner = Model.insert(
            name=self.contact_name or self.name,
            type=type
        )
        return partner
