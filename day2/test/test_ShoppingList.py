import unittest
from Designs.app import shoppingList

class test_shoppingList(unittest.TestCase):
    def setUp(self):
        self.shoppingList = shoppingList()
    
    def test_user_has_entered_shopping_list_name(self):
        self.assertRaises(ValueError, self.shoppingList.shoppingListName, '')
    
    def test_user_has_entered_shopping_list_description(self):
        self.assertRaises(ValueError, self.shoppingListDescription, '')
        

if __name__ == '__main__':
    unittest.main()