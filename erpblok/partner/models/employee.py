from anyblok import Declarations
from anyblok.column import Integer, String, Date


register = Declarations.register
Model = Declarations.Model


@register(Model.Partner.Individual)
class Employee:

    id = Integer(primary_key=True, foreign_key=Model.Partner.Individual.use("id"))
    employee_id = String()
    job_title = String()
    hire_date = Date()

    def get_display_name(self):
        name = super(Employee, self).get_display_name()
        if self.job_title:
            return f"{name} ({self.job_title})"

        return name
