#!/usr/bin/python3
""" Test Base for Base Class """

import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    """Testing"""

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_base(self):
        """creating a new instance and check for id"""

        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base()
        self.assertEqual(b2.id, 2)
        b3 = Base()
        self.assertEqual(b3.id, 3)
        b4 = Base(12)
        self.assertEqual(b4.id, 12)
        b5 = Base(4)
        self.assertEqual(b5.id, 4)

    def test_base_type(self):
        """Test for type and instance"""

        b6 = Base()
        self.assertEqual(type(b6), Base)
        self.assertTrue(isinstance(b6, Base))

if __name__ == '__main__':
    unittest.main()
