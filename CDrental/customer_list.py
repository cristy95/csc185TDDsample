class Customer_list(object):
	def __init__(self):
		self.customers = {}

	def add_customer(self, customer1):
		self.customers[customer1.customer_id] = customer1.name

	def get_customer(self, customer_id):
		if self.customers.get(customer_id) is None:
			return "None"
		else:
			return self.customers[customer_id]
			