from anyblok import Declarations


register = Declarations.register
Model = Declarations.Model


@register(Model.PurchaseOrder)
class PurchaseOrder:

    def action_confirm(self):
        super(PurchaseOrder, self).action_confirm()
        self.generate_stock_moves()

    def generate_stock_moves(self):
        move_obj = self.anyblok.Model.StockMove
        # Simplified: get default locations
        source = self.anyblok.Model.Location.get_first() # Should be a vendor location
        dest = self.anyblok.Model.Location.get_first() # Should be an internal location
        
        if not source or not dest:
            return

        for line in self.lines:
            if line.product.is_storable():
                move_obj.insert(
                    product=line.product,
                    qty=line.qty,
                    source_location=source,
                    dest_location=dest,
                )
