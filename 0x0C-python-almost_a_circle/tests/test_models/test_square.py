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

    def test_sq_area(self):
        """ """
        s1 = Square(3)
        self.assertEqual(s1.area(), 9)
        s2 = Square(10)
        self.assertEqual(s2.area(), 100)
        s3 = Square(8, 0, 0, 12)
        self.assertEqual(s3.area(), 64)

    def test_sq_str_(self):
        """ """
        s1 = Square(4, 2, 1, 12)
        self.assertEqual(s1.__str__(), "[Square] (12) 2/1 - 4")
        s2 = Square(5, 1)
        self.assertEqual(s2.__str__(), "[Square] (1) 1/0 - 5")


    def test_sq_size(self):
        """ """
        s1 = Square(5)
        self.assertEqual(s1.__str__(), "[Square] (1) 0/0 - 5")
        self.assertEqual(s1.size, 5)
        s1.size = 10
        self.assertEqual(s1.__str__(), "[Square] (1) 0/0 - 10")
        with self.assertRaises(TypeError):
            s1.size = "9"

    def test_sq_update(self):
        """ """
        s1 = Square(5)
        self.assertEqual(s1.__str__(), "[Square] (1) 0/0 - 5")
        s1.update(10)
        self.assertEqual(s1.__str__(), "[Square] (10) 0/0 - 5")
        s1.update(1, 2)
        self.assertEqual(s1.__str__(), "[Square] (1) 0/0 - 2")
        s1.update(1, 2, 3)
        self.assertEqual(s1.__str__(), "[Square] (1) 3/0 - 2")
        s1.update(1, 2, 3, 4)
        self.assertEqual(s1.__str__(), "[Square] (1) 3/4 - 2")
        s1.update(x=12)
        self.assertEqual(s1.__str__(), "[Square] (1) 12/4 - 2")
        s1.update(size=7, y=1)
        self.assertEqual(s1.__str__(), "[Square] (1) 12/1 - 7")
        s1.update(size=7, id=89, y=1)
        self.assertEqual(s1.__str__(), "[Square] (89) 12/1 - 7")
