#!/usr/bin/python3
"""testing cases ( file storage )"""

import unittest
import os
from models.engine.file_storage import FileStorage

class TestFileStorage(unittest.TestCase):
    """Set up test environment before each test case"""
def testcase1(self):
		testobj = FileStorage()
		testobj.__file_path
		self.assertTrue(os.path.isfile(testobj))
