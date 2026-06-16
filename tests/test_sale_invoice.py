import pytest


@pytest.mark.anyblok_setup
class TestSaleInvoice:

    def test_sale_to_invoice_flow(self, db_session, system):
        Individual = system.anyblok.Model.Partner.Individual
        Product = system.anyblok.Model.Product
        Order = system.anyblok.Model.Sale.Order
        OrderLine = system.anyblok.Model.Sale.OrderLine
        
        # Setup data
        partner = Individual.insert(name="Customer", type="individual")
        product = Product.insert(name="Good", product_type="product", list_price=10.0)
        
        # Create Order
        order = Order.insert(partner=partner, type="standard", state="draft")
        OrderLine.insert(order=order, product=product, qty=5, price_unit=10.0)
        
        # Confirm Order
        order.action_confirm()
        assert order.state == "confirmed"
        
        # Create Invoice
        invoice = order.create_invoice()
        assert invoice is not None
        assert invoice.partner == partner
        assert len(invoice.lines) == 1
        assert invoice.lines[0].product == product
        assert invoice.lines[0].qty == 5
        assert invoice.lines[0].price_unit == 10.0
