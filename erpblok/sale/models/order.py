from anyblok import Declarations
from anyblok.column import Integer, String, Selection, Date, Float
from anyblok.relationship import Many2One


register = Declarations.register
Model = Declarations.Model
Mixin = Declarations.Mixin


@register(Model)
class Sale:
    pass


@register(Model.Sale)
class Order(Mixin.AuditMixin, Mixin.DocumentMixin):

    id = Integer(primary_key=True)
    type = String(nullable=False)
    partner = Many2One(model='Model.Partner', nullable=False)
    date = Date(nullable=False)
    state = Selection(selections='get_states', default='draft', nullable=False)
    amount_total = Float(default=0.0)

    @classmethod
    def get_states(cls):
        return {
            'draft': 'Draft',
            'sent': 'Sent',
            'confirmed': 'Confirmed',
            'done': 'Done',
        }

    def action_confirm(self):
        if self.state in ('draft', 'sent'):
            self.state = 'confirmed'
            for line in self.lines:
                if not line.price_unit:
                    line.price_unit = line.product.get_price(line.qty, self.partner)

    @classmethod
    def define_mapper_args(cls):
        mapper_args = super(Order, cls).define_mapper_args()
        if cls.__registry_name__ == 'Model.Sale.Order':
            mapper_args.update({
                'polymorphic_on': cls.type,
            })

        mapper_args.update({
            'polymorphic_identity': cls.__registry_name__,
        })

        return mapper_args
