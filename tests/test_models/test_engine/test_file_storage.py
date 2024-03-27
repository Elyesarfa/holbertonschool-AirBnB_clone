#!/usr/bin/python3
"""Testing cases for FileStorage"""

import unittest
import os
from models.engine.file_storage import FileStorage

class TestFileStorage(unittest.TestCase):
    """Test cases for FileStorage"""

    def setUp(self):
        """Set up test environment before each test case"""
        self.testobj = FileStorage()

    def tearDown(self):
        """Clean up test environment after each test case"""
        del self.testobj
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_file_path_exists(self):
        """Test if file path exists"""
        testobj = FileStorage()
        self.assertTrue(os.path.isfile(self.testobj._FileStorage__file_path))

if __name__ == '__main__':
    unittest.main()
