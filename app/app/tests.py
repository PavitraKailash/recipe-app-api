"""Sample Tests"""

from django.test import SimpleTestCase
from app import calc


class CalcTests(SimpleTestCase):
    """Test the Calc Module"""

    def test_add_numbers(self):
        """Test adding numbers together"""
        res = calc.add(6, 5)
        self.assertEqual(res, 11)
           
    def test_subtract_numbers(self):
        res = calc.subtract(10, 15)
        self.assertEqual(res, 5)
