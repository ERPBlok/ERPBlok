from anyblok import Declarations
from anyblok.column import Integer, Float, Date, Selection
from anyblok.relationship import Many2One


register = Declarations.register
Model = Declarations.Model


@register(Model)
class Contract:

    id = Integer(primary_key=True)
    employee = Many2One(model='Model.Partner.Individual.Employee', nullable=False)
    company = Many2One(model='Model.Partner.Company', nullable=False)
    wage = Float(default=0.0)
    start_date = Date(nullable=False)
    end_date = Date()
    struct_type = Selection(selections='get_struct_types', default='cdi', nullable=False)

    @classmethod
    def get_struct_types(cls):
        return {
            'cdi': 'CDI',
            'cdd': 'CDD',
            'internship': 'Internship',
        }
