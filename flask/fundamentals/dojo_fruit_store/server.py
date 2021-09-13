from flask import Flask, render_template, request, redirect
from flask.globals import session
app = Flask(__name__)
app.secret_key = 'jfdsklajfksljfnaklvnewrkdvne'

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    print(request.form)
    session['f_name'] = request.form['first_name']
    session['l_name'] = request.form['last_name']
    session['student_id'] = request.form['student_id']
    session['straw_no'] = request.form['strawberry']
    session['rasp_no'] = request.form['raspberry']
    session['apple_no'] = request.form['apple']
    quantity = int(request.form['strawberry']) + int(request.form['raspberry']) + int(request.form['apple'])
    print(f'Charging {session["f_name"]} for {quantity} fruits.')
    return render_template("checkout.html", quantity = quantity)

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    