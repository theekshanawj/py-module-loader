import unittest

class TestGreaterThan(unittest.TestCase):

	def test_three_greater_than_two(self):
		self.assertTrue(3 > 2)



if __name__ == '__main__':
	unittest.main()
