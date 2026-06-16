from anyblok import Declarations
from anyblok.column import Integer, String, Float


register = Declarations.register
Model = Declarations.Model
Mixin = Declarations.Mixin


@register(Model)
class Product(Mixin.AuditMixin):

    id = Integer(primary_key=True)
    product_type = String(nullable=False)
    name = String(nullable=False)
    list_price = Float(default=0.0)
    standard_price = Float(default=0.0)

    def is_storable(self):
        return False

    def get_price(self, qty, partner):
        return self.list_price

    def get_purchase_price(self, qty, partner):
        return self.standard_price

    @classmethod
    def define_mapper_args(cls):
        mapper_args = super(Product, cls).define_mapper_args()
        if cls.__registry_name__ == 'Model.Product':
            mapper_args.update({
                'polymorphic_on': cls.product_type,
            })
        mapper_args.update({
            'polymorphic_identity': cls.__registry_name__,
        })

        return mapper_args
