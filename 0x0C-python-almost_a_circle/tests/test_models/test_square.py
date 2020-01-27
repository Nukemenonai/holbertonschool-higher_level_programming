#!/usr/bin/python3
""" test file bor base class """

import unittest

from models.base import Base
from models.square import Square

class Test_id(unittest.TestCase):

    """ """
    def setUp(self):
            Base._Base__nb_objects = 0

    def test_id(self):
        """ test id of a rectangle """
        s1 = Square(2)
        self.assertEqual(s1.id, 1)
        s2 = Square(10)
        self.assertEqual(s2.id, 2)
        s3 = Square(10, 0, 0, 12)
        self.assertEqual(s3.id, 12)

    def test_attributes(self):
        """ """
        with self.assertRaises(TypeError):
            Square("2")
        with self.assertRaises(ValueError):
            s = Square(2)
            s.width = -10
        with self.assertRaises(TypeError):
            s = Square(2)
            s.x = {}
        with self.assertRaises(ValueError):
            Square(10, 3, -1)
