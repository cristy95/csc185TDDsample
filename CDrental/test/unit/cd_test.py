import unittest
from cd import CD

class TestCD(unittest.TestCase):
	def test_cd_can_be_created(self):
		cd1 = CD("Beatles", "Unrented")
		self.assertEqual(cd1.cd_id, "Beatles")
		self.assertEqual(cd1.cd_status, "Unrented")

	def is_rented(self):
		cd1 = CD("Beatles", "Unrented")
		self.assertEqual(cd1.cd_status(cd1), "Unrented")