from flask import Flask, render_template
app = Flask(__name__)  


@app.route('/')
def basic_i():
    return render_template('basic_i.html', y=8, x=8, odd_color='blueviolet', even_color='purple')

@app.route('/<int:y>')
def basic_ii(y):
    return render_template('basic_i.html', y=y, x=8, odd_color='blueviolet', even_color='purple')

@app.route('/<int:y>/<int:x>')
def basic_iii(y, x):
    return render_template('basic_i.html', y=y, x=x, odd_color='blueviolet', even_color='purple')

@app.route('/<int:y>/<int:x>/<string:odd_color>/<string:even_color>')
def basic_iiii(y, x, odd_color, even_color):
    print(type(odd_color))
    print(type(even_color))
    return render_template('basic_i.html', y=y, x=x, odd_color=odd_color, even_color=even_color)


if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)