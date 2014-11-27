import unittest
from cd_rental import CD_rental
from checkout import Checkout
from cd import CD
from cd_list import CDList
from customer import Customer

class Test_CD_rental(unittest.TestCase):
	def test_cd_rental_is_initially_empty(self):
		cd_rent = CD_rental()
		self.assertEqual({}, cd_rent.checkouts)

	def test_add_checkout(self):
		cd_rent = CD_rental()
		cd_list1 = CDList()
		cd1 = CD("Beatles", "Unrented")
		customer1 = Customer("001", "Kringot")
		cd_list1.add_cd(cd1)
		cd1.is_rented()
		checkout1 = Checkout(customer1.customer_id, customer1.name, cd1.cd_id, "11/25/14", "11/27/14")
		self.assertEqual(cd1.is_rented(), "Unrented")

		cd_rent.add_checkout(checkout1)
		cd1.change_status()

		self.assertEqual(cd_rent.checkouts[checkout1.customer_id].customer_id, "001")
		self.assertEqual(cd_rent.checkouts[checkout1.customer_id].name, "Kringot")
		self.assertEqual(cd_rent.checkouts[checkout1.customer_id].cd_id, "Beatles")
		self.assertEqual(cd_rent.checkouts[checkout1.customer_id].date, "11/25/14")
		self.assertEqual(cd_rent.checkouts[checkout1.customer_id].due_date, "11/27/14")
		self.assertEqual(cd1.is_rented(), "Rented")
		self.assertEqual(len(cd_rent.checkouts), 1)

	def test_get_checkout_record(self):
		cd_rent = CD_rental()
		cd_list1 = CDList()
		cd1 = CD("Beatles", "Unrented")
		customer1 = Customer("001", "Kringot")
		checkout1 = Checkout(customer1.customer_id, customer1.name, cd1.cd_id, "11/25/14", "11/27/14")

		cd_list1.add_cd(cd1)
		cd1.is_rented()
		cd_rent.add_checkout(checkout1)
		cd1.change_status()

		self.assertEqual(cd_rent.get_checkout_record(checkout1).customer_id, "001")
		self.assertEqual(cd_rent.get_checkout_record(checkout1).name, "Kringot")
		self.assertEqual(cd_rent.get_checkout_record(checkout1).cd_id, "Beatles")
		self.assertEqual(cd_rent.get_checkout_record(checkout1).date, "11/25/14")
		self.assertEqual(cd_rent.get_checkout_record(checkout1).due_date, "11/27/14")