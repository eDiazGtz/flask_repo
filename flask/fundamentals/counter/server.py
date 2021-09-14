from flask import Flask, render_template, session, redirect
from flask.globals import request

# F12 -> Application -> Cookies -> http://localhost... -> session -> DELETE

app = Flask(__name__)
app.secret_key = 'jfkldsjnfgikojewrn0oi484308'

@app.route('/')
def counter():
    if 'count' not in session:
        session['count'] = 0
        session['int'] = 0
    session['count'] += 1
    return render_template('counter.html')

@app.route('/count')
def count():
    return redirect('/')

@app.route('/two')
def two():
    session['count'] += 1
    session['int'] += 2
    return redirect('/')

@app.route('/form', methods=['POST'])
def form():
    if request.form['int'] == '':
        request.form['int'] = 0
    session['count'] += int(request.form['int']) - 1
    session['int'] += int(request.form['int'])
    return redirect('/')

@app.route('/destroy')
def destroy():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)