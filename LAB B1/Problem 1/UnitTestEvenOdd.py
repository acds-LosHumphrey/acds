#-------------------------------------------------------------------------------
# Name:        Unit Test 1
# Purpose:
#
# Author:      okre1
#
# Created:     08/02/2018
# Copyright:   (c) okre1 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import unittest


class NumbersTest(unittest.TestCase):

    def test_even(self):

        #Test that numbers between 0 and 5 are all even.

        for i in range(0, 6):
            with self.subTest(i=i):
                self.assertEqual(i % 2, 0)


    def test_odd(self):

        #Test that numbers between 0 and 5 are all odd.

        for i in range(0, 6):
            with self.subTest(i=i):
                self.assertEqual(i % 2, 1)


if __name__ == '__main__':
    unittest.main()