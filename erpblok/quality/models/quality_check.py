from anyblok import Declarations
from anyblok.column import Integer, Selection, Text
from anyblok.relationship import Many2One


register = Declarations.register
Model = Declarations.Model
Mixin = Declarations.Mixin


@register(Model)
class QualityCheck(Mixin.AuditMixin):

    id = Integer(primary_key=True)
    product = Many2One(model='Model.Product', nullable=False)
    point = Many2One(model='Model.QualityPoint', nullable=False)
    result = Selection(selections='get_results', nullable=True)
    notes = Text()
    state = Selection(selections='get_states', default='draft', nullable=False)

    @classmethod
    def get_results(cls):
        return {
            'pass': 'Pass',
            'fail': 'Fail',
        }

    @classmethod
    def get_states(cls):
        return {
            'draft': 'Draft',
            'done': 'Done',
        }

    def action_done(self):
        if not self.result:
            raise ValueError("Result must be set before finishing the check")
        
        self.state = 'done'
        
        if self.result == 'fail':
            self.anyblok.Model.QualityAlert.insert(
                check=self,
                description=f"Quality check failed for {self.product.name}"
            )
