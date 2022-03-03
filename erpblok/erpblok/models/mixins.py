from anyblok import Declarations
from anyblok.field import Function
from anyblok.column import (
    Integer, String, Country, Selection, PhoneNumber, URL, Email)


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
    value = Function(fget="get_value")
    label = String(nullable=False)
    phone = PhoneNumber()
    url = URL()
    email = Email()

    def get_value(self):
        if self.type in ('phone', 'mobile', 'fax'):
            return self.phone

        if self.type in ('website',):
            return self.url

        if self.type in ('email',):
            return self.email

    @classmethod
    def get_types(cls):
        return {
            'phone': 'Phone',
            'mobile': 'Mobile',
            'fax': 'Fax',
            'email': 'E-Mail',
            'website': 'Website',
        }

    def type_validator_phone(self):
        if not self.phone:
            raise Exception('the field phone is required')

    type_validator_mobile = type_validator_phone
    type_validator_fax = type_validator_phone

    def type_validator_email(self):
        if not self.email:
            raise Exception('the field email is required')

    def type_validator_website(self):
        if not self.url:
            raise Exception('the field url is required')

    @classmethod
    def before_update_orm_event(cls, mapper, connection, target):
        type_validator_method = f"type_validator_{target.type}"
        if hasattr(target, type_validator_method):
            getattr(target, type_validator_method)()
