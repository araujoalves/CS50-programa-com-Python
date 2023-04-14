import unittest
from numb3rs import validate


class MyTestCase(unittest.TestCase):
    def test_passed(self):
        self.assertTrue(validate('255.0.0.0'))
        self.assertTrue(validate('244.199.97.0'))

    def test_failed(self):
        self.assertFalse(validate('28.264.183.94'))
        self.assertFalse(validate('268.476.783.946'))
        self.assertFalse(validate('cat:cats'))
        self.assertFalse(validate('2684.0.1718.4698'))


if __name__ == '__main__':
    unittest.main()
