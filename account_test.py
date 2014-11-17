import unittest
from account import Account

class TestAccount(unittest.TestCase):
  def test_account_object_can_be_created(self):
    account = Account("001", 50)
    self.assertEqual(account.account_number, "001")
    self.assertEqual(account.balance, 50)
    
  def test_account_with_string_balance(self):
  	account = Account("001", "hey")
  	self.assertEqual(account.account_number, "Undefined")
  	self.assertEqual(account.balance, "Wrong Parameter")
  	
if __name__ == '__main__':
  unittest.main()
