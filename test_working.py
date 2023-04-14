import unittest
from working_9_to_5 import convert


class MyTestCase(unittest.TestCase):
    def test_input(self):
        with self.assertRaises(ValueError):
            convert('9:60 AM to 5:60 PM')
        with self.assertRaises(ValueError):
            convert('9 AM - 5 PM')
        with self.assertRaises(ValueError):
            convert('9 AM 5 PM')

    def test_invalid(self):
        with self.assertRaises(ValueError):
            convert('to')

    def test_out_of_range(self):
        with self.assertRaises(ValueError):
            convert('13:00 AM to 13:00 PM')

    def test_omit_to(self):
        with self.assertRaises(ValueError):
            convert('6:19 AM 4:20 PM')

    def test_convert(self):
        self.assertEqual(convert('9 AM to 5 PM'), '09:00 to 17:00')
        self.assertEqual(convert('9:00 AM to 5:00 PM'), '09:00 to 17:00')
        self.assertEqual(convert('10 PM to 8 AM'), '22:00 to 08:00')
        self.assertEqual(convert('10:30 PM to 8:50 AM'), '22:30 to 08:50')


if __name__ == '__main__':
    unittest.main()
