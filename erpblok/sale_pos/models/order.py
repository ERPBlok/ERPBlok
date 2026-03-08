from anyblok import Declarations
from anyblok.column import Integer, String


register = Declarations.register
Model = Declarations.Model


@register(Model.Sale.Order)
class PosOrder:

    id = Integer(primary_key=True, foreign_key=Model.Sale.Order.use("id"))
    session_id = String(nullable=False)

    def action_confirm(self):
        super(PosOrder, self).action_confirm()
        self.state = 'done'
