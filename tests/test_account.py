import pytest


@pytest.mark.anyblok_setup
class TestAccount:

    def test_account_move_balance(self, db_session, system):
        Account = system.anyblok.Model.Account
        Journal = system.anyblok.Model.Journal
        Move = system.anyblok.Model.AccountMove
        MoveLine = system.anyblok.Model.AccountMoveLine
        Company = system.anyblok.Model.Partner.Company
        
        # Setup
        company = Company.insert(name="My Co", type="company")
        journal = Journal.insert(name="General", code="GN", company=company)
        acc_a = Account.insert(name="Asset", code="1000", company=company)
        acc_b = Account.insert(name="Income", code="7000", company=company)
        
        # Create balanced move
        move = Move.insert(journal=journal, date=system.anyblok.anyblok_date.today())
        MoveLine.insert(move=move, account=acc_a, debit=100.0, credit=0.0)
        MoveLine.insert(move=move, account=acc_b, debit=0.0, credit=100.0)
        
        # Verify
        assert move.total_debit == 100.0
        assert move.total_credit == 100.0
        assert move.total_debit == move.total_credit
