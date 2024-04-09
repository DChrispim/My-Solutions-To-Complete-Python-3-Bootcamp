import unittest
from animal_crackers import *

class TestAnimalCrackers(unittest.TestCase):

    def test_original_1(self):
        result = animal_crackers('Levelheaded Llama')
        self.assertEqual(result, True)

    def test_original_2(self):
        result = animal_crackers('Levelheaded llama')
        self.assertEqual(result, True)

    def test_original_3(self):
        result = animal_crackers('Crazy Kangaroo')
        self.assertEqual(result, False)

if __name__ == '__main__':
    unittest.main()
