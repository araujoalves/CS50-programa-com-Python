import unittest
from regular_um_expressions import count


class MyTestCase(unittest.TestCase):
    def test_word(self):
        self.assertEqual(count('yummy'), 0)
        self.assertEqual(count('bum'), 0)

    def test_um_beginning(self):
        self.assertEqual(count('um'), 1)
        self.assertEqual(count('um...'), 1)
        self.assertEqual(count('um, hello'), 1)
        self.assertEqual(count('UM, hello'), 1)
        self.assertEqual(count('um'), 1)
        self.assertEqual(count('um, hello, um, world'), 2)
        self.assertEqual(count('um, um, um'), 3)

    def test_um_middle(self):
        self.assertEqual(count('hello, um, world'), 1)
        self.assertEqual(count('hello um world um'), 2)

    def test_um_end(self):
        self.assertEqual(count('hello, um'), 1)
        self.assertEqual(count('hello, hm world, um'), 1)

    def test_none(self):
        self.assertEqual(count('hello, world'), 0)
        self.assertEqual(count('hello'), 0)


if __name__ == '__main__':
    unittest.main()
