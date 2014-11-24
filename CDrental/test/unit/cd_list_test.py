import unittest
from cd_list import CDList
from cd import CD

class TestCDList(unittest.TestCase):
	def test_cd_list_is_initially_empty(self):
		cdlist1 = CDList()
		self.assertEqual(len(cdlist1.cdlist), 0)

	def test_add_cd_list(self):
		cdlist1 = CDList()
		cd1 = CD("Beatles", "Unrented")

		cdlist1.add_cd(cd1)
		self.assertEqual(len(cdlist1.cdlist), 1)