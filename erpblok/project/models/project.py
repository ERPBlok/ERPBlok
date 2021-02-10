from anyblok.declarations import Declarations
from anyblok.column import String, Color, Sequence, Text
# from anyblok_pyramid.bloks.pyramid.restrict import restrict_query_by_user


@Declarations.register(Declarations.Model.ERPBlok)
class Project:

    code = Sequence(primary_key=True, formater="P{seq:010d}")
    label = String(nullable=False)
    color = Color()
    description = Text()
