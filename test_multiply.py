from unittest import TestCase
from multiply import mul

class testMultuplyCase(TestCase):
    def test_valid(self):
        res = mul(2, 2)
        self.assertEqual(res, 4)
