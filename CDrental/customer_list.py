class Customer_list(object):
	def __init__(self):
		self.customers = {}

	def add_customer(self, customer1):
		self.customers[customer1.customer_id] = customer1.name