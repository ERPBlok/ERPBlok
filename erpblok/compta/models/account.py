from anyblok.declarations import Declarations
from anyblok.column import String, Text
from anyblok.relationship import Many2One


@Declarations.register(Declarations.Model.ERPBlok)
class Account:

    code = String(primary_key=True, size=20)
    label = String(nullable=False)

    # model n'utilise pas la declaration car elle
    # n'existe pas encore
    parent = Many2One(model='Model.ERPBlok.Account',
                      one2many="children")
    description = Text()
