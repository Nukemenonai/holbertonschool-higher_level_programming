""" test file bor base class """

import unittest

from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class Test_id(unittest.TestCase):

    """ """
    def setUp(self):
        Base.__nb_objects = 0

    def test_init(self):
        """ test init """
        Base.__nb_objects = 0
        b1 = Base()
        self.assertEqual(print(b1.id), 1)
        b2 = Base()
        self.assertEqual(print(b2.id), 2)
        b3 = Base()
        self.assertEqual(print(b3.id), 3)
        b4 = Base(12)
        self.assertEqual(print(b4.id), 12)
        b5 = Base()
        self.assertEqual(print(b5.id), 4)

if __name__ == '__main__':
    unittest.main()
