class Bank(object):
	def __init__(self):
		self.accounts = {}

	def add_account(self, account):
		if account.balance == "hey":
			return "Wrong Parameter"
		else:
			self.accounts[account.account_number] = account.balance
	
if __name__ == '__main__':
	unittest.main()