from anyblok import Declarations
from anyblok.column import Integer, String
from anyblok.relationship import Many2One


register = Declarations.register
Model = Declarations.Model
Mixin = Declarations.Mixin


@register(Model)
class Vehicle(Mixin.AuditMixin):

    id = Integer(primary_key=True)
    name = String(nullable=False)
    license_plate = String(nullable=False)
    driver = Many2One(model='Model.Partner')

    def get_tco(self):
        """Calculate Total Cost of Ownership
        """
        Fuel = self.anyblok.Model.VehicleLogFuel
        InvoiceLine = self.anyblok.Model.Invoice.InvoiceLine
        
        # Fuel costs
        fuel_cost = Fuel.query().filter(Fuel.vehicle == self).sum(Fuel.amount) or 0.0
        
        # Purchase invoices linked to the vehicle
        invoice_cost = InvoiceLine.query().filter(
            InvoiceLine.vehicle == self,
            InvoiceLine.invoice.type == 'in_invoice'
        ).sum(InvoiceLine.price_subtotal) or 0.0
        
        return fuel_cost + invoice_cost
