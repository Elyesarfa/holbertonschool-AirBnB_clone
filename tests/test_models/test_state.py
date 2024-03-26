#!/usr/bin/python3
"""Unit tests for State class"""

import unittest
from models.state import State


class TestState(unittest.TestCase):
    """Test cases for State class"""

    def test_attributes(self):
        """Test State attributes"""
        x = State()
        self.assertTrue(isinstance(x.name, str))
