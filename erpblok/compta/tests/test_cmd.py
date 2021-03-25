"""Test expected state once demo data are installed"""
import pytest


@pytest.mark.usefixtures("rollback_registry")
class TestMove:
    """ Test database state after installed demo data"""

    def test_get_balance(self, rollback_registry):
        registry = rollback_registry
        Move = registry.ERPBlok.Account.Move
        Header = Move.Header

        query = Move.query().join(Move.header)
        query = query.filter(Header.reference == 'facture 1')

        move = query.first()
        assert move is not None

        assert move.get_balance() == move.credit  # because debit = 0

    def test_get_amount(self, rollback_registry):
        registry = rollback_registry
        Header = registry.ERPBlok.Account.Move.Header

        query = Header.query()
        query = query.filter(Header.reference == 'facture 1')

        header = query.one()
        assert header.get_amount() == 1200  # because debit = 0
