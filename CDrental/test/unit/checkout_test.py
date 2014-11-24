import unittest
from checkout import Checkout

class TestCheckout(unittest.TestCase):
	def test_checkout_can_be_created(self):
		checkout1 = Checkout("001", "Beatles")
		self.assertEqual(checkout1.customer_id, "001")
		self.assertEqual(checkout1.cd_id, "Beatles")