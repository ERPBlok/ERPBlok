from anyblok import Declarations
from anyblok.column import Integer, String, Country, Selection


register = Declarations.register
Mixin = Declarations.Mixin


@register(Mixin)
class ERPBlokAddress:

    id = Integer(primary_key=True)
    name = String()
    street = String(nullable=False)
    street_2 = String()
    street_3 = String()
    zip_code = String(nullable=False)
    city = String(nullable=False)
    country = Country(nullable=False, mode='alpha_3')

    @classmethod
    def before_update_orm_event(cls, mapper, connection, target):
        country_validator_method = (
            f"country_validator_{target.country.alpha_3.lower()}")
        if hasattr(target, country_validator_method):
            getattr(target, country_validator_method)()


@register(Mixin)
class ERPBlokContact:

    id = Integer(primary_key=True)
    type = Selection(selections="get_types", nullable=False)
    value = String(nullable=False)
    label = String(nullable=False)

    @classmethod
    def get_types(cls):
        return {
        }

    @classmethod
    def before_update_orm_event(cls, mapper, connection, target):
        type_validator_method = f"type_validator_{target.type}"
        if hasattr(target, type_validator_method):
            getattr(target, type_validator_method)()
