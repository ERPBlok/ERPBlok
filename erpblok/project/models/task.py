from anyblok.declarations import Declarations
from anyblok.column import String, Sequence, Text, Selection, Integer
from anyblok.relationship import Many2One
# from anyblok_pyramid.bloks.pyramid.restrict import restrict_query_by_user


@Declarations.register(Declarations.Model.ERPBlok.Project)
class Task:

    code = Sequence(primary_key=True, formater="T{seq:010d}")
    project = Many2One(model=Declarations.Model.ERPBlok.Project, nullable=False,
                       one2many="tasks")
    label = String(nullable=False)
    order = Integer(nullable=False, default=0)
    description = Text()
    state = Selection(selections={
        'draft': 'Draft',
        'backlog': 'Backlog',
        'inprogress': 'In progress',
        'done': 'Done',
        'inprod': 'In production',
    }, default='draft')
