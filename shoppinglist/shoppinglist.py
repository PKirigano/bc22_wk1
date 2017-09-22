from flask import Flask
import pickle
from shoppingList.user import addUser
from shoppingList.shoppingList import addShoppingList
app = Flask(__name__)

@app.route('/signup')
def signup():
    if request.method = 'post':
        addUser.userName = request.form['userName']
        addUser.email = request.form['email']
        addUser.password = request.form['password']
        addUser.gender = request.form['gender']

with open('user_data.pkl', 'wb') as output:
    user_data = addUser(userName, email, password, gender)
    pickle.dump(user_data, output, pickle.HIGHEST_PROTOCOL)

del user_data

@app.route('/signin')
def signin():
    if request.method = 'get':
        with open('shopping_list', 'rb') as input:
            user_list = pickle.load(in)
        
if __name__=="__main__":
    app.run()