#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_Integer(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_voidlist(self):
        self.assertEqual(max_integer([]), None)

    def test_equal_elements(self):
        self.assertEqual(max_integer([4, 4, 4, 4]), 4)
        self.assertEqual(max_integer([-4, -4, -4, -4]), -4)

    def test_matrix_zero(self):
        self.assertEqual(max_integer([0]), 0)

    def test_letters(self):
        self.assertEqual(max_integer(['a', 'b', 'c', 'd']), 'd')

    def test_hybrid_list(self):
        with self.assertRaises(TypeError):
            self.assertEqual(max_integer(['a', 'b', 4, 2]), 'b')

    def test_exceed_param_number(self):
        with self.assertRaises(TypeError):
            self.assertEqual(max_integer(2,4), 4)
