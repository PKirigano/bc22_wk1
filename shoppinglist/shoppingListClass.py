class shoppingList(object):
    def __init__(self, shoppingListName, shoppingListDescription):
        self.shoppingListName = shoppingListName
        self.shoppingListDescription = shoppingListDescription
    
    def addShoppingList(self, shoppingListName, shoppingListDescription):
        shoppinglist = shoppingList()

class user(object):
    def __init__(self userName, email, passWord, gender):
        self.userName = userName
        self.email = email
        self.passWord = passWord
        self.gender = gender
    