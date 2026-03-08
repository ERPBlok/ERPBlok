from anyblok import Declarations


register = Declarations.register
Model = Declarations.Model


@register(Model.Stock)
class Move:

    def check_availability(self):
        """Extended with quality checks blocking logic
        """
        QualityCheck = self.anyblok.Model.QualityCheck
        
        # Search for pending or failed quality checks for this product
        checks = QualityCheck.query().filter(
            QualityCheck.product == self.product,
            QualityCheck.state != 'done'
        ).all()
        
        if checks:
            raise ValueError(f"Stock move blocked: {len(checks)} quality checks are pending for {self.product.name}")
            
        # Also block if the latest check failed (if we want to be strict)
        last_check = QualityCheck.query().filter(
            QualityCheck.product == self.product,
            QualityCheck.state == 'done'
        ).order_by(QualityCheck.id.desc()).first()
        
        if last_check and last_check.result == 'fail':
            raise ValueError(f"Stock move blocked: Last quality check for {self.product.name} failed")

        return True
