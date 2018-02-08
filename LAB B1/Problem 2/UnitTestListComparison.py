#-------------------------------------------------------------------------------
# Name:        Unit test 2
# Purpose:
#
# Author:      okre1
#
# Created:     08/02/2018
# Copyright:   (c) okre1 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import unittest




class ListTest(unittest.TestCase):
    def setUp(self):
        super(ListTest, self).setUp()
        self.addTypeEqualityFunc(str, self.assertMultiLineEqual)

    def testString(self):
        a = [1, 1, 2, 2, 3, 5, 8, 13, 21, 34, 55, 89]
        b = [1, 2, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

        for count in range(max(len(a),len(b))):
            for counte in range(max(len(a),len(b))):
                with self.subTest(count=count+counte):
                    self.assertEqual(a[count], b[counte])


if __name__ == '__main__':
    unittest.main()