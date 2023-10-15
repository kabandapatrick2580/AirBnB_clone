#!/usr/bin/python3
from models.user import User
import unittest

class TestUser(unittest.TestCase):
    def test_instance_creation(self):
        """Test if an instance of User is created successfully"""
        user = User()
        self.assertIsInstance(user, User)

    def test_attributes(self):
        """Test if User has the expected attributes"""
        user = User()
        self.assertTrue(hasattr(user, 'email'))
        self.assertTrue(hasattr(user, 'password'))
        self.assertTrue(hasattr(user, 'first_name'))
        self.assertTrue(hasattr(user, 'last_name'))

    def test_default_values(self):
        """Test if the attributes have default values"""
        user = User()
        self.assertEqual(user.email, '')
        self.assertEqual(user.password, '')
        self.assertEqual(user.first_name, '')
        self.assertEqual(user.last_name, '')

if __name__ == "__main__":
    unittest.main()
