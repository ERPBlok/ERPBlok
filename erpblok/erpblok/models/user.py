from anyblok.declarations import Declarations
from anyblok.column import Boolean
from anyblok.relationship import Many2One


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

    def restrict_by_companies(self, query, company_field):
        Company = self.anyblok.Company
        query = query.join(company_field)
        query = query.filter(
            Company.name.in_([
                useraccess.company.name
                for useraccess in self.companies_accesses]))

        return query
