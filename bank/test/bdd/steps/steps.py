from lettuce import *

from account import Account
from bank import Bank

@step(u'account number 0001 is a valid account')
def _valid_account(step):
	account = Account(0001, 50)
	bank = Bank()
	bank.add_account(account)