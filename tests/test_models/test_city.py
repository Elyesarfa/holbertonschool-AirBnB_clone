#!/usr/bin/python3
"""Unit tests for City class"""

import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """Test cases for City class"""

    def test_attributes(self):
        x = City()
        self.assertTrue(isinstance(x.name, str))
        self.assertTrue(isinstance(x.state_id, str))
