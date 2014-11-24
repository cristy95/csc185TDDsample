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
		checkout1 = Checkout(customer1, cd1)

		cd_list1.add_cd(cd1)
		cd1.is_rented()
		cd_rent.add_checkout(checkout1)
		cd1.change_status()

		self.assertEqual(checkout1.customer1.customer_id, "001")
		self.assertEqual(checkout1.customer1.name, "Kringot")
		self.assertEqual(checkout1.cd1.cd_id, "Beatles")
		self.assertEqual(checkout1.cd1.cd_status, "Rented")
		self.assertEqual(len(cd_rent.checkouts), 1)