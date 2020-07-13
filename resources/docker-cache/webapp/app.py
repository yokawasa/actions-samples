import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def ok():
    return 'OK'

@app.route('/version')
def version():
    ver = 'NONE'
    with open('VERSION','r') as f:
        ver = f.read()
    return "I am {}".format(ver)

if __name__ == '__main__':
    # Bind to MYVERSION_PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('MYVERSION_PORT', 5000))
    app.run(host='0.0.0.0', port=port)
