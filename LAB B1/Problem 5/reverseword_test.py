import unittest
import reverseword 

class TestReverse(unittest.TestCase):

	def test_reverse_true(self):
		result = reverseword.reverse("una oracion")
		self.assertEqual(result, "oracion una")

	def test_reverse_false(self):
		result = reverseword.reverse("una oracion")
		self.assertNotEqual(result,"una oracion")

if __name__ == '__main__':
    unittest.main()
