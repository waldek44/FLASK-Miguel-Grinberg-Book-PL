from flask import Flask
app = Flask(__name__)


@app.route('/')
def index():
    return '<p> to jest hello </p>'


# wprowadzam do paska http://127.0.0.1:5000/user/superman
@app.route('/user/<name>')
def user(name):
    return '<p> Witaj {} </p>'.format(name)
