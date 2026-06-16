import pytest


@pytest.mark.anyblok_setup
class TestPartner:

    def test_individual_polymorphism(self, db_session, system):
        Partner = system.anyblok.Model.Partner
        Individual = system.anyblok.Model.Partner.Individual
        
        # Create an individual
        ind = Individual.insert(
            name="John Doe",
            firstname="John",
            lastname="Doe",
            gender="male",
            type="individual"
        )
        db_session.commit()
        
        # Check that it's also a partner
        partner = Partner.get(ind.id)
        assert partner is not None
        assert partner.name == "John Doe"
        assert partner.type == "individual"
        
        # Check specific fields
        assert ind.firstname == "John"
        assert ind.lastname == "Doe"

    def test_company_polymorphism(self, db_session, system):
        Partner = system.anyblok.Model.Partner
        Company = system.anyblok.Model.Partner.Company
        
        # Create a company
        comp = Company.insert(
            name="Any Corp",
            siret="123456789",
            vat_number="FR123456789",
            type="company"
        )
        db_session.commit()
        
        # Check that it's also a partner
        partner = Partner.get(comp.id)
        assert partner is not None
        assert partner.name == "Any Corp"
        assert partner.type == "company"
        
        # Check specific fields
        assert comp.siret == "123456789"
