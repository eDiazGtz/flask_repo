from flask import Flask, render_template

app = Flask(__name__)    # Create a new instance of the Flask class called "app"


@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return 'Hello World!'  # Return the string 'Hello World!' as a response

@app.route('/dojo')
def dojo():
    return 'Dojo!'

@app.route('/say/<string:name>')
def greeting(name):
    print(type(name))
    return f'Hi {name}'

@app.route('/repeat/<int:repeat>/<string:line>')
def repeat(repeat, line):
    return f'{repeat*line}'

@app.route('/<catchall>')
def catch_all(catchall):
    return 'Sorry! No response. Try again.'

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)