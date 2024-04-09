import unittest
from old_macdonald import *


class TestOldMacdonald(unittest.TestCase):

    def test_original_1(self):
        result = old_macdonald('macdonald')
        self.assertEqual(result, 'MacDonald')
    
    def test_long_name(self):
        result = old_macdonald('longname')
        self.assertEqual(result, 'LonGname')
    
    def test_short_name(self):
        with self.assertRaises(Exception) as context:
            old_macdonald('sho')

        self.assertTrue("Use a string name greater than 3." in str(context.exception))


if __name__ == '__main__':
    unittest.main()
