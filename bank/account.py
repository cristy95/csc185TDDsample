class Account(object):
	def __init__(self, account_number, balance):

		if type(balance) == int:
			self.account_number = account_number
			self.balance = balance
		else:
			self.account_number = "Undefined"
			self.balance = "Wrong Parameter"

if __name__ == '__main__':
	unittest.main()

