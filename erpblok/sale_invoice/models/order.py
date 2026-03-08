from anyblok import Declarations


register = Declarations.register
Model = Declarations.Model


@register(Model.Sale.Order)
class Order:

    def create_invoice(self):
        invoice_obj = self.anyblok.Model.Invoice
        line_obj = self.anyblok.Model.InvoiceLine
        
        # Determine company (simple fallback)
        company = getattr(self, 'company', None) or self.partner.company # Assuming link exists
        
        invoice = invoice_obj.insert(
            partner=self.partner,
            date=self.anyblok.anyblok_date.today(),
            company=company,
            state='draft'
        )
        
        for line in self.lines:
            line_obj.insert(
                invoice=invoice,
                product=line.product,
                qty=line.qty,
                price_unit=line.price_unit,
                # account would ideally come from product/category
            )
            
        return invoice
