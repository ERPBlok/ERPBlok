from anyblok import Declarations
from anyblok.column import Integer, Float, String
from anyblok.relationship import Many2One, One2Many


register = Declarations.register
Model = Declarations.Model
Mixin = Declarations.Mixin


@register(Model)
class BOM(Mixin.AuditMixin):

    id = Integer(primary_key=True)
    name = String(nullable=False)
    product = Many2One(model='Model.Product', nullable=False)
    qty = Float(default=1.0, nullable=False)
    lines = One2Many(model='Model.BOMLine', backref='bom')


@register(Model)
class BOMLine(Mixin.AuditMixin):

    id = Integer(primary_key=True)
    bom = Many2One(model='Model.BOM', nullable=False)
    product = Many2One(model='Model.Product', nullable=False)
    qty = Float(default=1.0, nullable=False)
