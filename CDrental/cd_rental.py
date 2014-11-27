class CD_rental(object):
	def __init__(self):
		self.checkouts = {}

	def add_checkout(self, checkout):		
		self.checkouts[checkout.customer_id] = checkout

	def get_checkout_record(self, checkout1):
		self.checkouts[checkout1.customer_id] = checkout1
		ans = self.checkouts[checkout1.customer_id]
		return ans