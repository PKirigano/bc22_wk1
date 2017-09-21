import unittest
import shoppingList
import user

class test_shoppingList(unittest.TestCase):
    def setUp(self):
        self.shoppingList = shoppingList()
    
    def test_user_has_entered_shopping_list_name(self):
        self.assertRaises(ValueError, self.shoppingList.shoppingListName, '')
    
    def test_user_has_entered_shopping_list_description(self):
        self.assertRaises(ValueError, self.shoppingListDescription, '')


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
        

if __name__ == '__main__':
    unittest.main()