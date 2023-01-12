from unittest import TestCase
from summ import sum

class testSummCase(TestCase):
    def test_valid(self):
        res = sum(3, 2)
        self.assertEqual(res, 5)
