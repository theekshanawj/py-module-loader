import unittest

class TestLessThan(unittest.TestCase):

	def test_three_less_than_2(self):
		self.assertFalse(3 < 2)
