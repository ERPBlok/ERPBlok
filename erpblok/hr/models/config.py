from anyblok import Declarations
from anyblok.column import Boolean
from anyblok_furetui.field import Contextual
from anyblok_furetui.factory import SingletonModelFactory


register = Declarations.register
Model = Declarations.Model


@register(Model.Company.Employee, factory=SingletonModelFactory)
class Configuration:

    must_be_link_with_a_user = Contextual(
        Boolean(default=False), identity='company')

    @classmethod
    def define_contextual_models(cls):
        return {
            'company': {
                'model': cls.anyblok.Company,
            }
        }
