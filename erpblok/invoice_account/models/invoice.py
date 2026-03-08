from anyblok import Declarations


register = Declarations.register
Model = Declarations.Model


@register(Model.Invoice)
class Invoice:

    def action_post(self):
        super(Invoice, self).action_post()
        self.generate_account_move()

    def generate_account_move(self):
        # Extremely simplified accounting logic for demonstration
        aml_obj = self.anyblok.Model.Account.Move.Line
        move_obj = self.anyblok.Model.Account.Move
        
        # We assume some default journals and accounts exist for the demo
        journal = self.anyblok.Model.Journal.get_first() # Placeholder
        if not journal:
            return

        move = move_obj.insert(
            name=self.number or f"INV/{self.id}",
            date=self.date,
            journal=journal,
            company=self.company,
            currency=self.company.currency # Placeholder
        )

        total = 0
        for line in self.lines:
            subtotal = line.price_unit * line.qty
            aml_obj.insert(
                move=move,
                account=line.account,
                partner=self.partner,
                credit=subtotal
            )
            total += subtotal

        # Balancing entry (Receivable)
        receivable_account = self.anyblok.Model.Account.get_first(type='receivable') # Placeholder
        if receivable_account:
            aml_obj.insert(
                move=move,
                account=receivable_account,
                partner=self.partner,
                debit=total
            )
