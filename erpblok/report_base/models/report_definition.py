from anyblok import Declarations
from anyblok.column import Integer, String, Text, Selection


register = Declarations.register
Model = Declarations.Model


@register(Model)
class ReportDefinition:

    id = Integer(primary_key=True)
    name = String(nullable=False)
    query = Text(nullable=False)
    type = Selection(selections='get_types', default='sql', nullable=False)

    @classmethod
    def get_types(cls):
        return {
            'sql': 'Raw SQL',
            'sqlalchemy': 'SQLAlchemy Expression',
        }
