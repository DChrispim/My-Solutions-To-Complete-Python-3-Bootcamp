import unittest
from ran_check import *

class TestRanCheckVerbose(unittest.TestCase):
    def test_is_between(self):
        result = ran_check_verbose(5,2,7)
        self.assertTrue(result == '5 is in the range between 2 and 7')
    
    def test_is_not_between(self):
        result = ran_check_verbose(5,6,7)
        self.assertTrue(result == '5 is not in the range between 6 and 7')

class TestRanCheckBoolean(unittest.TestCase):
    def test_is_between(self):
        self.assertTrue(ran_check_boolean(3,1,10))
    
    def test_is_not_between(self):
        self.assertFalse(ran_check_boolean(3,4,10))

if __name__ == '__main__':
    unittest.main()
