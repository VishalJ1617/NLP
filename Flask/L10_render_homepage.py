from flask import Flask, render_template, request

app = Flask(__name__, template_folder = 'templates')

@app.route('/')
def student():
    return render_template('L10_Homepage.html')

@app.route('/result', methods = ['GET', 'POST'])
def result():
    if request.method == 'POST':
        m1 = int(request.form['phy'])
        m2 = int(request.form['chem'])
        m3 = int(request.form['maths'])
        avg = (m1 + m2 + m3) / 3
        temp = {}
        temp['name'] = request.form['name']
        temp['average'] = avg
    return render_template('L10_result_for_loop.html', result=temp)


if __name__ == '__main__':
    app.run(debug = True)