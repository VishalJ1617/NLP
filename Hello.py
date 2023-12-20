from flask import Flask
app = Flask(__name__)   # Initializing the flask object

@app.route('/hello/<name>')  # values within the <> are varibles, given at the runtime
def hello_me(name):
    return 'Hi <b>%s</b> Welcome to Pune!' %name   # <b>x</b> x will be printed in bold, HTML tag

if __name__ == '__main__':
    app.run(debug=True)