class Checkout(object):
	def __init__(self, customer_id, name, cd_id, date, due_date):
		self.customer_id = customer_id
		self.name = name
		self.cd_id = cd_id
		self.date = date
		self.due_date = due_date