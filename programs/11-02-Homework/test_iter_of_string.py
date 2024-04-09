import unittest
from iter_of_string import *

class TestIterOfString(unittest.TestCase):

    def test_iter_of_string(self):
        word = 'hello'
        result = []
        for n in iter_of_string(word):
            result.append(n)
        
        self.assertEqual(result, list(word))

if __name__ == '__main__':
    unittest.main()
