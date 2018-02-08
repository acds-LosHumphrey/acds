import unittest
import cowsbulls 

class Testcowsbulls(unittest.TestCase):

	def test_cowsbulls_true(self):
		cowsbulls.defineAnswerManually("1234")
		result = cowsbulls.evaluateWord("1234")
		self.assertEqual(result, [4,4])

if __name__ == '__main__':
    unittest.main()