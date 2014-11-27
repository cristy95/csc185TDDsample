import unittest
from checkout import Checkout
from cd import CD
from customer import Customer

class TestCheckout(unittest.TestCase):
	def test_checkout_can_be_created(self):
		cd1 = CD("Beatles", "Unrented")
		customer1 = Customer("001", "Kringot")
		checkout1 = Checkout(customer1.customer_id, customer1.name, cd1.cd_id, "11/25/14", "11/27/14")
		self.assertEqual(checkout1.customer_id, "001")
		self.assertEqual(checkout1.name, "Kringot")
		self.assertEqual(checkout1.cd_id, "Beatles")
		self.assertEqual(checkout1.date, "11/25/14")
		self.assertEqual(checkout1.due_date, "11/27/14")


