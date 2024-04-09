import unittest
import pytest
from print_big import *

class TestPrintBig(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def _pass_fixtures(self, capsys):
        self.capsys = capsys

    def test_A(self):
        print_big('a')
        captured = self.capsys.readouterr()
        self.assertEqual('  *  \n * * \n*****\n*   * \n*   * ', captured.out)
