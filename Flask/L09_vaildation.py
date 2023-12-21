from flask import Flask, request, redirect, url_for

app = Flask(__name__)

admin_id = 'admin'
admin_password = 'admin'

@app.route('/success/<name>')
def success(name):
   return 'Welcome %s!' %name

@app.route('/unsuccessful')
def unsuccessful():
   return "Invalid ID or password"

@app.route('/login', methods=['GET', 'POST'])
def admin():
   if request.method == 'POST':
       user_id = request.form['user_id']
       password = request.form['password']
       if user_id == admin_id and password == admin_password:
           return redirect(url_for('success', name=admin_id))
       else:
           return redirect(url_for('unsuccessful'))


if __name__ == '__main__':
   app.run(debug=True)
