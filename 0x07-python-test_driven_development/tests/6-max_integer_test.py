#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_int_list(self):
        self.assertEqual(max_integer([1, 2, 3]), 3)
        self.assertEqual(max_integer([1, 3, 2]), 3)
        self.assertEqual(max_integer([3, 2, 1]), 3)
        self.assertEqual(max_integer([-1, 0, 1]), 1)
        self.assertEqual(max_integer([-1, -1, -1]), -1)
        self.assertEqual(max_integer([3]), 3)

    def test_float_list(self):
        self.assertEqual(max_integer([1.2, 2.3, 3.4]), 3.4)
        self.assertEqual(max_integer([1.1, 3.0, 2.5]), 3.0)
        self.assertEqual(max_integer([3.5, 2.1, 7.1]), 7.1)

    def test_string_list(self):
        self.assertEqual(max_integer(["Jack", "Sparrow"]), "Sparrow")
        self.assertEqual(max_integer("Jack"), "k")
        self.assertEqual(max_integer(""), None)

    def test_float_list(self):
        self.assertEqual(max_integer([1.2, 2.3, 3.4]), 3.4)
        self.assertEqual(max_integer([1.1, 3.0, 2.5]), 3.0)
        self.assertEqual(max_integer([3.5, -2.1, 7.1]), 7.1)
