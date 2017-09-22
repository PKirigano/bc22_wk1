from flask import Flask
from shopingList.user import addUser
from shoppingList.shoppingList import addShoppingList
app = Flask(__name__)

@app.route('/signup')
def signup():
    if request.method = 'post':
        addUser.userName = request.form['userName']
        addUser.email = request.form['email']
        addUser.password = request.form['password']
        addUser.gender = request.form['gender']

@app.route('/signin')
def signin():
    if request.method = 'put':
        
if __name__=="__main__":
    app.run()