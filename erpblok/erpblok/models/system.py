from anyblok import Declarations
from anyblok.column import Selection
from anyblok.relationship import Many2One
from anyblok_pyramid.bloks.pyramid.restrict import restrict_query_by_user


register = Declarations.register
System = Declarations.Model.System


@register(System)
class Sequence:

    company = Many2One(model='Model.Company', nullable=False)
    type = Selection(selections='get_types', nullable=False)

    @classmethod
    def get_default_values(cls, *a, **kw):
        res = super(Sequence, cls).get_default_values(*a, **kw)
        res['company'] = cls.context.get('company')
        if cls.__registry_name__ != 'Model.System.Sequence':
            res['type'] = cls.__registry_name__

        return res

    @classmethod
    def get_types(cls):
        return {}

    @classmethod
    def define_mapper_args(cls):
        mapper_args = super(Sequence, cls).define_mapper_args()
        if cls.__registry_name__ == 'Model.System.Sequence':
            mapper_args.update({'polymorphic_on': cls.type})
            mapper_args.update({'polymorphic_identity': None})
        else:
            mapper_args.update({'polymorphic_identity': cls.__registry_name__})

        return mapper_args

    @restrict_query_by_user()
    def restrict_by_company(cls, query, user):
        return user.restrict_by_company(query, cls.company)
