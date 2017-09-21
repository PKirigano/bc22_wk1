from flask import Flask
app = Flask(__name__)

@app.route("/")
def shopingList():

if __name__=="__main__":
    app.run()