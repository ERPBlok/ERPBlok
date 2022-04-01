from anyblok.declarations import Declarations
from anyblok.column import Boolean
from anyblok.relationship import Many2One
from sqlalchemy import func


registrer = Declarations.register
Model = Declarations.Model


@Declarations.register(Model.Company)
class UserAccess:

    user = Many2One(model=Model.Pyramid.User, primary_key=True,
                    one2many="companies_accesses",
                    foreign_key_options={'ondelete': 'cascade'})

    company = Many2One(model=Model.Company, primary_key=True,
                       foreign_key_options={'ondelete': 'cascade'})

    can_create = Boolean(default=True)
    can_update = Boolean(default=True)
    can_delete = Boolean(default=True)


@Declarations.register(Declarations.Model.Pyramid)
class User:

    current_company = Many2One(model=Model.Company, nullable=False)

    def restrict_by_companies(self, query, company_field):
        Company = self.anyblok.Company
        query_with_companies = query.join(
            company_field).filter(
            Company.id.in_([
                useraccess.company.id
                for useraccess in self.companies_accesses])
        )
        query_without_company = query.outerjoin(
            company_field).group_by(
            self.anyblok.get(query.Model)).having(
            func.count(Company.id) == 0)

        return query_with_companies.union(query_without_company)

    def restrict_by_company(self, query, company_field):
        Company = self.anyblok.Company
        query = query.join(company_field)
        query = query.filter(Company.id == self.current_company.id)
        return query


@Declarations.register(Declarations.Model)
class FuretUI:

    @classmethod
    def set_user_context(cls, authenticated_userid):
        super(FuretUI, cls).set_user_context(authenticated_userid)
        user = cls.context['user']
        cls.context.set({
            'company': user.current_company,
        })
