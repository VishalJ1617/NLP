### ----------------
### Import statement
### ----------------

from flask import Flask


app = Flask(__name__)   # Initializing the flask object

@app.route('/square/<num>')  # values within the <> are varibles, given at the runtime
def hello_me(num):
    sq = int(num) ** 2
    return 'Square of %s is <b>%d</b>' %(num,sq)   # <b>x</b> x will be printed in bold, HTML tag


if __name__ == '__main__':
    app.run(debug=True)