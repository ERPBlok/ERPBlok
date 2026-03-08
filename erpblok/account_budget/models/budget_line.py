from anyblok import Declarations
from anyblok.column import Integer, Float
from anyblok.relationship import Many2One


register = Declarations.register
Model = Declarations.Model
Mixin = Declarations.Mixin


@register(Model.Budget)
class Line(Mixin.AuditMixin):

    id = Integer(primary_key=True)
    budget = Many2One(model=Model.Budget, nullable=False, one2many="lines")
    account = Many2One(model=Model.Account, nullable=False)
    planned_amount = Float(default=0.0)
    practical_amount = Float(default=0.0)

    def _compute_practical_amount(self):
        """Calculate Practical Amount from accounting lines
        """
        MoveLine = self.anyblok.Model.Account.Move.Line
        
        # We assume move.date exists and is the criteria
        # Based on refactoring, Line belongs to Account.Move
        query = MoveLine.query().filter(
            MoveLine.account == self.account,
            MoveLine.move.date >= self.budget.date_from,
            MoveLine.move.date <= self.budget.date_to
        )
        
        debits = query.sum(MoveLine.debit) or 0.0
        credits = query.sum(MoveLine.credit) or 0.0
        
        self.practical_amount = debits - credits
        return self.practical_amount
