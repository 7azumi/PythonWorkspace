import unittest
from sum_sub import mysum
from sum_sub import mysub


class Test(unittest.TestCase):
    def setUp(self):
        print("Unit test started")
    def tearDown(self):
        print("Unit test end")

    def test_mysum(self):
        self.assertEqual(mysum(1,5),6,"加法有误")

    def test_mysub(self):
        self.assertEqual(mysub(7,3),4,"减法有误")

if __name__ == "__main__":
    unittest.main()
