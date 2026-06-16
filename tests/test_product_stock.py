import pytest


@pytest.mark.anyblok_setup
class TestProductStock:

    def test_product_is_storable_injection(self, db_session, system):
        Service = system.anyblok.Model.Product.Service
        StorableProduct = system.anyblok.Model.Product.StorableProduct
        
        # Test Service (should be False)
        serv = Service.insert(name="Consulting", product_type="service")
        assert serv.is_storable() is False
        
        # Test StorableProduct (should be True)
        prod = StorableProduct.insert(name="Laptop", product_type="storableproduct")
        assert prod.is_storable() is True

    def test_product_prices(self, db_session, system):
        Product = system.anyblok.Model.Product
        prod = Product.insert(
            name="Test Product", 
            product_type="product",
            list_price=100.0,
            standard_price=50.0
        )
        
        assert prod.get_price(1, None) == 100.0
        assert prod.get_purchase_price(1, None) == 50.0
