import unittest
import overlap


class Testoverlap(unittest.TestCase):

 """
    Return a list containing the elements which are in both primernumbers and happynumbers

    >>> overlap([2,3,5,7,11,13,17,19,23,29,31,37,41,43,47], [1,7,10,13,19,23,28,31,32,44,49,68,70,79,82])
    [7,13,19,23,31]
"""
    def test_overlap_numbers(primenumbers, happynumbers):
       result = []
    for element in primenumbers:
        if element in happynumbers:
            result.append(element)
    return result

if __name__ == '__main__':
    unittest.main()
