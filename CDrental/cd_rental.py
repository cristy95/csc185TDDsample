class CD_rental(object):
	def __init__(self):
		self.checkouts = {}

	def add_checkout(self, checkout):
		
		self.checkouts[checkout.customer_id] = checkout.cd_id