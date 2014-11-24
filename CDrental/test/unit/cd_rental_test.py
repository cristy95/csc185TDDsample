import unittest
from cd_rental import CD_rental
from checkout import Checkout
from cd import CD
from cd_list import CDList

class Test_CD_rental(unittest.TestCase):
	def test_cd_rental_is_initially_empty(self):
		cd_rent = CD_rental()
		self.assertEqual({}, cd_rent.checkouts)

	def test_add_checkout(self):
		cd_rent = CD_rental()
		cd_list1 = CDList()
		checkout1 = Checkout("001", "Beatles")
		cd1 = CD("Beatles", "Unrented")

		cd_list1.add_cd(cd1)
		cd1.is_rented(cd1)
		cd_rent.add_checkout(checkout1)
		cd_list1.change_status(cd1)


		self.assertEqual(len(cd_rent.checkouts), 1)

