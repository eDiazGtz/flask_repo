from flask import Flask, render_template, session, request
app = Flask(__name__)
app.secret_key = 'hjtgu9i345g385jhg30ghjn3i3'

@app.route('/')
def form():
    return render_template('form.html')

@app.route('/result', methods = ['POST'])
def result():
    session['name'] = request.form['name']
    session['dojo'] = request.form['dojo']
    session['lang'] = request.form['lang']
    session['comm'] = request.form['comm']
    return render_template('results.html')

if __name__=='__main__':
    app.run(debug=True)