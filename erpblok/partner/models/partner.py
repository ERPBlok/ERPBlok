from anyblok import Declarations
from anyblok.column import Integer, String, Boolean


register = Declarations.register
Model = Declarations.Model
Mixin = Declarations.Mixin


@register(Model)
class Partner(Mixin.AuditMixin):

    id = Integer(primary_key=True)
    type = String(nullable=False)
    name = String(nullable=False)
    email = String()
    phone = String()
    is_company = Boolean(default=False)
    active = Boolean(default=True)

    def get_display_name(self):
        return self.name

    @classmethod
    def define_mapper_args(cls):
        mapper_args = super(Partner, cls).define_mapper_args()
        if cls.__registry_name__ == 'Model.Partner':
            mapper_args.update({
                'polymorphic_on': cls.type,
                'polymorphic_identity': 'partner',
            })
        else:
            mapper_args.update({
                'polymorphic_identity': cls.__registry_name__.lower().split('.')[-1],
            })

        return mapper_args
