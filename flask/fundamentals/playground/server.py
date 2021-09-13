from flask import Flask, render_template, redirect

app = Flask(__name__)  

@app.route('/')
def index():
    return redirect('/play')

@app.route('/play')
def play():
    return render_template('index.html', num=3, color="blue")

@app.route('/play/<int:num>')
def num(num):
    return render_template('index.html', num=num, color="purple")

@app.route('/play/<int:num>/<string:color>')
def num_and_color(num, color):
    return render_template('index.html', num=num, color=color)

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)