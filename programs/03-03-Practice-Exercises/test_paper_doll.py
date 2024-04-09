import unittest
from paper_doll import *


class TestPaperDoll(unittest.TestCase):

    def test_original_1(self):
        result = paper_doll('Hello')
        self.assertEqual(result, 'HHHeeellllllooo')

    def test_original_2(self):
        result = paper_doll('Mississippi')
        self.assertEqual(result, 'MMMiiissssssiiissssssiiippppppiii')

if __name__ == '__main__':
    unittest.main()
