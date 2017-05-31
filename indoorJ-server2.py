from flask import Flask, request
import os

app = Flask(__name__)
#app.run(host='0.0.0.0')
app.debug = True

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/hello')
def hello():
    return 'TuT_'

@app.route('/file', methods=['POST', 'GET'])
def update_file():
    if request.method == 'POST':
        # Get file object from field of file
        f = request.files['userfile']
        f.save(os.path.join('C:\\Users\\Nova\\Desktop', f.filename))
        # Get str object from field of text
        s = request.form['name']
        with open('/home/ping/Documents/test.txt', 'a') as f:
            f.write(s)
    return 'Done!'

if __name__ == '__main__':
    app.run()
