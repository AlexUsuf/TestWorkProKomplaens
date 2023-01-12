from unittest import TestCase
from subtraction import sub

class testSubtractionCase(TestCase):
    def test_valid(self):
        res = sub(4, 4)
        self.assertEqual(res, 0)
