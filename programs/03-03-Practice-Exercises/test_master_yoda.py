import unittest
from master_yoda import *

class TestMasterYoda(unittest.TestCase):

    def test_original_1(self):
        result = master_yoda('I am home')
        self.assertEqual(result, 'home am I')
    
    def test_original_2(self):
        result = master_yoda('We are ready')
        self.assertEqual(result, 'ready are We')
    
    def test_one_word_phrase(self):
        result = master_yoda('Ready!')
        self.assertEqual(result, 'Ready!')

if __name__ == '__main__':
    unittest.main()
