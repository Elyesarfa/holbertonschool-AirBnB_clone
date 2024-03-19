#!/usr/bin/python3
"""testing cases ( basemodel )"""

from models.base_model import BaseModel
from models import storage
import unittest
import os
import models


class TestCases(unittest.TestCase):
    """testing cases"""
    def test_case_save(self):
        """testing save"""
        test1 = BaseModel()
        old = test1.updated_at
        test1.save()
        new = test1.updated_at
        self.assertNotEqual(old, new)
        self.assertTrue(os.path.exists(models.storage._FileStorage__file_path))

    def test_case_dict(self):
        """testing __dict__"""
        test1 = BaseModel()
        x = test1.__class__.__name__
        dictionary = test1.__dict__.copy()
        test_dictionary = test1.to_dict()
        self.assertAlmostEqual(dictionary["id"], test1.id)
        self.assertAlmostEqual(dictionary["created_at"], test1.created_at)
        self.assertAlmostEqual(dictionary["updated_at"], test1.updated_at)
        self.assertAlmostEqual(test_dictionary["__class__"], x)

    def test_case_str(self):
        """testing __str__"""
        test1 = BaseModel()
        string = str(f"[{test1.__class__.__name__}] ")
        string = string + f"({test1.id}) {test1.__dict__}"
        self.assertEqual(test1.__str__(), string)

if __name__ == '__main__':
    unittest.main()
