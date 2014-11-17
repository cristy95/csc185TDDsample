import unittest
from account import Account
from bank import Bank

class BankTest(unittest.TestCase):
  def test_bank_is_initially_empty(self):
    bank = Bank()
    self.assertEqual({}, bank.accounts)
    self.assertEqual(len(bank.accounts), 0)

 
  

if __name__ == '__main__':
	unittest.main()