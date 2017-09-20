import unittest
from app import user

class test_user(unittest.TestCase):
    def setUp(self):
        self.user = user()

    def test_userName_has_been_entered(self):
        self.assertRaises(ValueError, self.user.userName, '')
    
    def test_email_has_been_entered(self):
        self.assertRaises(ValueError, self.user.email, '')
    
    def test_password_has_been_entered():
        self.assertRaises(ValueError, self.user.passWord, '')

    def test_gender_has_been_entered():
        self.assertRaises(ValueError, self.user.gender, '')