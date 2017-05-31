from flask import Flask

app = Flask(__name__)
#app.run(host='0.0.0.0')
app.debug = True

@app.route('/')
def hello_world():
    return 'Hello World!'
@app.route('/hello')
def hello():
    return 'TuT_'

if __name__ == '__main__':
    app.run()
