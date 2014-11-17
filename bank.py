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



if __name__ == '__main__':
	unittest.main()