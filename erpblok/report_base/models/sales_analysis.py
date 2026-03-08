from anyblok import Declarations
from anyblok.column import Integer, String, Float
from sqlalchemy import select, func, text, join
from anyblok.model.factory import ViewFactory


register = Declarations.register
Model = Declarations.Model


@register(Model, factory=ViewFactory)
class SalesAnalysis:
    """Sales Analysis View
    """

    id = Integer(primary_key=True)
    month = String()
    category = String()
    product_name = String()
    partner_name = String()
    total_qty = Float()
    total_amount = Float()

    @classmethod
    def sqlalchemy_view_declaration(cls):
        # Setup the selectable
        Order = cls.anyblok.Sale.Order
        Line = cls.anyblok.Sale.OrderLine
        Product = cls.anyblok.Product
        Partner = cls.anyblok.Partner
        
        # For simplicity in this example, we use a basic SQL construction
        # In a real AnyBlok app, we might use a proper sqlalchemy.sql.selectable
        selectable = select(
            [
                func.row_number().over().label('id'),
                func.to_char(Order.date, 'YYYY-MM').label('month'),
                Product.product_type.label('category'),
                Product.name.label('product_name'),
                Partner.name.label('partner_name'),
                func.sum(Line.qty).label('total_qty'),
                func.sum(Line.qty * Line.price_unit).label('total_amount'),
            ]
        ).select_from(
            join(Order, Line, Order.id == Line.order_id).join(
                Product, Line.product_id == Product.id
            ).join(
                Partner, Order.partner_id == Partner.id
            )
        ).group_by(
            text('month'), 
            Product.product_type, 
            Product.name, 
            Partner.name
        ).alias('sales_analysis_view')

        return selectable
