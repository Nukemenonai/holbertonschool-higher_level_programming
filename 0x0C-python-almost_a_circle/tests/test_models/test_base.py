import unittest

from models.base import Base

class Test_id(unittest.TestCase):

    def test_init(self):
        """ test base class """
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

