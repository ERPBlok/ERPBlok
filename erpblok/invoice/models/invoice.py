from anyblok import Declarations
from anyblok.column import Integer, String, Selection, Date
from anyblok.relationship import Many2One


register = Declarations.register
Model = Declarations.Model
Mixin = Declarations.Mixin


@register(Model)
class Invoice(Mixin.AuditMixin, Mixin.DocumentMixin):

    id = Integer(primary_key=True)
    number = String()
    partner = Many2One(model='Model.Partner', nullable=False)
    date = Date(nullable=False)
    state = Selection(selections='get_states', default='draft', nullable=False)
    company = Many2One(model='Model.Partner.Company', nullable=False)

    @classmethod
    def get_states(cls):
        return {
            'draft': 'Draft',
            'posted': 'Posted',
            'paid': 'Paid',
            'cancelled': 'Cancelled',
        }

    def action_post(self):
        if self.state == 'draft':
            self.state = 'posted'
            # Hook for invoice_account bridge
