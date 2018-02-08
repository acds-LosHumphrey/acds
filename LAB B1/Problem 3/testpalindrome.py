import unittest
import palindrome


class TestPalindrome(unittest.TestCase):

    def test_is_palindrome_true(self):
        value = palindrome.is_palindrome('racecar')
        self.assertEquals(value, True)

    def test_is_palindrome_false(self):
        value = palindrome.is_palindrome('dedent')
        self.assertEquals(value, False)

    def test_reverse_normal(self):
        value = palindrome.reverse('hello')
        self.assertEquals(value, 'olleh')

    def test_reverse_error(self):
        list_of_bad_value = [
        123,
        None,
        ]
        for bad_value in list_of_bad_value:
            self.assertRaises(
                TypeError,
                palindrome.reverse,
                bad_value
            )

if __name__ == '__main__':
    unittest.main()
