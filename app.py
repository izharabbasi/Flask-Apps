from flask import Flask,jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello! You Are On The Main Page </h1>'

@app.route('/home',methods=['POST','get'], defaults={'name':'izhar'})
@app.route('/home/<name>', methods=['POST','GET'])
def home(name):
    return '<h1>Hello {}, you are on the Home Page</h1>'.format(name)


@app.route('/Profile')
def profile():
    return '<h1>Hello you are on the Profile Page</h1>'

@app.route('/json')
def json():
    return jsonify({'key':'value', 'key2':[1,2,3,4]})

if __name__ == '__main__':
    app.run()
