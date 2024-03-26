#!/usr/bin/python3
"""testing cases ( user )"""

from models.user import User
import unittest


class testcases(unittest.TestCase):
	def testcase1(self):
		x = User()
		self.assertTrue(isinstance(x.email, str))
		self.assertTrue(isinstance(x.password, str))
		self.assertTrue(isinstance(x.first_name, str))
		self.assertTrue(isinstance(x.last_name, str))
