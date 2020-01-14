#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Set of cases to test a function that returns a max integer
    from a list of integers
    """
    def test_Integer(self):
        """ tests only integers"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_max_beginning(self):
        """tests max at the beggining"""
        self.assertEquals(max_integer([5, 4, 3, 2]), 5)

    def test_voidlist(self):
        """tests a void list"""
        self.assertEqual(max_integer([]), None)

    def test_equal_elements(self):
        """tests for equal elements inside a list"""
        self.assertEqual(max_integer([4, 4, 4, 4]), 4)
        self.assertEqual(max_integer([-4, -4, -4, -4]), -4)

    def test_matrix_zero(self):
        """tests when the only item is zero"""
        self.assertEqual(max_integer([0]), 0)

    def test_letters(self):
        """Tests a list of characters"""
        self.assertEqual(max_integer(['a', 'b', 'c', 'd']), 'd')

    def test_hybrid_list(self):
        """ Tests a mixed int - char list"""
        with self.assertRaises(TypeError):
            self.assertEqual(max_integer(['a', 'b', 4, 2]), 'b')

    def test_exceed_param_number(self):
        """ Tests when # of params is exceeded"""
        with self.assertRaises(TypeError):
            self.assertEqual(max_integer(2, 4), 4)

    def test_single_tuple(self):
        """ Tests a single tuple"""
        self.assertEqual(max_integer([(2, 4)]), (2, 4))

    def test_dual_tuple(self):
        """  Tests a double tuple"""
        self.assertEqual(max_integer([(1, 3), (4, 5)]), (4, 5))

    def test_true(self):
        """ Tests a list with a True Item"""
        self.assertEqual(max_integer([1,2,3,5,True]), 5)

    def test_complex(self):
        """ Testing a list with a complex number """
        with self.assertRaises(TypeError):
            max_integer([34, 78, 12, 5j])

    def test_hexa(self):
        """ Tests a list with a hexa number"""
        self.assertEqual(max_integer([12, 34, 56, 0xFFFFFF]), 16777215)
        self.assertEqual(max_integer([1234, 345, 0xFEDCBA]), 16702650)
