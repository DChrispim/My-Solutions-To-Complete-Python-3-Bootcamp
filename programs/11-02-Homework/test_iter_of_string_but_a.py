import unittest
from iter_of_string_but_a import *

class TestIterOfStringButA(unittest.TestCase):

    def test_iter_of_string_but_a(self):
        word = 'apple'
        result = []
        for n in iter_of_string_but_a(word):
            result.append(n)
        
        self.assertEqual(result, list('pple'))

if __name__ == '__main__':
    unittest.main()
