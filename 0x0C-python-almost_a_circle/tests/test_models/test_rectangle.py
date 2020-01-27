""" test file bor Rectangle class """

import unittest

from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class Test_id(unittest.TestCase):

    """ """
    def setUp(self):
        Base.__nb_objects = 0

    def test_id(self):
        """ test id of a rectangle """
        Base.__nb_objects = 0
        r1 = Rectangle(10, 2)
        self.assertEqual(print(r1.id), 1)
        r2 = Rectangle(2, 10)
        self.assertEqual(print(r2.id), 2)
        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(print(r3.id), 12)

    def test_attributes(self):
        """ """
        with self.assertRaises(TypeError):
            Rectangle(10, "2")
        with self.assertRaises(ValueError):
            r = Rectangle(10, 2)
            r.width = -10
        with self.assertRaises(TypeError):
            r = Rectangle(10, 2)
            r.x = {}
        with self.assertRaises(ValueError):
            Rectangle(10, 2, 3, -1)


if __name__ == '__main__':
    unittest.main()
