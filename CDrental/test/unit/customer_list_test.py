import unittest
from customer_list import Customer_list
from customer import Customer

class TestCustomerList(unittest.TestCase):
	def test_customer_list_is_initially_empty(self):
		customerlist1 = Customer_list()
		self.assertEqual(len(customerlist1.customers), 0)

	def test_add_customer(self):
		customerlist1 = Customer_list()
		customer1 = Customer("001", "Kringot")

		customerlist1.add_customer(customer1)

		self.assertEqual(customerlist1.customers[customer1.customer_id], customer1.name)
		self.assertEqual(len(customerlist1.customers), 1)