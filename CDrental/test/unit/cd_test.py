import unittest
from cd import CD

class TestCD(unittest.TestCase):
	def test_cd_can_be_created(self):
		cd1 = CD("Beatles", "Unrented")
		
		self.assertEqual(cd1.cd_id, "Beatles")
		self.assertEqual(cd1.cd_status, "Unrented")

	def test_is_rented(self):
		cd1 = CD("Beatles", "Unrented")

		self.assertEqual(cd1.cd_status, "Unrented")

	def test_change_status_to_rented(self):
		cd1 = CD("Beatles", "Unrented")

		cd1.change_status()

		self.assertEqual(cd1.cd_status, "Rented")