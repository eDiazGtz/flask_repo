from flask import Flask, session, redirect, render_template, request
import random
app = Flask(__name__)
app.secret_key = 'hjfg4328902405hrgu3h4oirg'

@app.route('/')
def game():
    if 'guess' not in session:
        session['guess'] = 'none'
        session['win'] = random.randint(1,100)
        session['tries'] = 5
    return render_template('game.html')

@app.route('/play', methods = ['POST'])
def play():
    session['tries'] -= 1
    session['last_guess'] = request.form['guess']
    if request.form['guess'] == '':
        session['guess'] = 'low'
        return redirect('/')
    if int(request.form['guess']) > session['win']:
        session['guess'] = 'high'
    elif int(request.form['guess']) < session['win']:
        session['guess'] = 'low'
    else:
        session['guess'] = 'correct'
    return redirect('/')

@app.route('/reset')
def reset():
    session.pop('guess')
    return redirect('/')

if __name__=='__main__':
    app.run(debug=True)