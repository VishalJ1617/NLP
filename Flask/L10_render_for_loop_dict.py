from flask import Flask, render_template

app = Flask(__name__, template_folder = 'templates')

@app.route('/result')
def result():
    data = {'phy' : 67, 'chem' : 75, 'math' : 98}
    return render_template('L10_result_for_loop.html', result = data)  # the variable name can be anything, not required to be 'result'


if __name__ == '__main__':
    app.run(debug = True)