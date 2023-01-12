from unittest import TestCase
from division import div

class testDivCase(TestCase):
    def test_valid(self):
        res = div(4, 2)
        self.assertEqual(res, 2)
