import unittest
from customer import Customer 

class TestCase(unittest.TestCase):
	def test_customer_is_created(self):
		customer1 = Customer("001", "Kringot")

		self.assertEqual(customer1.customer_id, "001")
		self.assertEqual(customer1.name, "Kringot")		