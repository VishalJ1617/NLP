### ----------------
### Import statement
### ----------------

from flask import Flask


app = Flask(__name__)   # Initializing the flask object

@app.route('/well')  
def welcome():
    return 'Welcome!'


@app.route('/good')  
def good():
    return 'Good bye all!'


@app.route('/')  
def home():
    return 'You are at home page'


if __name__ == '__main__':
    app.run(debug=True)