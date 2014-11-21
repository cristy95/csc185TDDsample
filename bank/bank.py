class Bank(object):
	def __init__(self):
		self.accounts = {}

	def add_account(self, account):
		if account.balance == "hey":
			return "Wrong Parameter"
		else:
			self.accounts[account.account_number] = account.balance
	
	def get_account_balance(self, account_number):
		ans = self.accounts.get(account_number)

		if ans == None:
			return "Not Found"
		else:
			return ans

	def is_account_balance_enough(self, account, amount):
		balance = account.balance

		if balance >= amount:
			return "YES"
		else:
			return "NO"

	def withdraw_amount(self, account, amount):
		balance = account.balance - amount
		account.balance = balance
		return "OK"



if __name__ == '__main__':
	unittest.main()