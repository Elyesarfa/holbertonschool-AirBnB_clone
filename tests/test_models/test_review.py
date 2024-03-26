#!/usr/bin/python3
"""Unit tests for Review class"""

import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """Test cases for Review class"""

    def test_attributes(self):
        x = Review()
        self.assertTrue(isinstance(x.place_id, str))
        self.assertTrue(isinstance(x.user_id, str))
        self.assertTrue(isinstance(x.text, str))
