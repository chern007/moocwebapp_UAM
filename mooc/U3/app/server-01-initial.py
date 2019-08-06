# -*- coding: UTF-8 -*-

import sys

from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    """
    It process the '/' url.
    :return: basic HTML
    """
    return "Hello Word! This is the answer of the server"


@app.route('/ex1')
def function_for_ex1():
    return 'Content of the url/ex1'


@app.route('/ex2')
def function_for_ex2():
    return '''
    
    <!DOCTYPE html>
    <html>
    
        <head>
            <title>ex2</title>
        </head>
    
        <body>
            <h1>ex2</h1>
        
            <p>Return to <a href="/">index</a></p>
        </body>

    </html>
    
    '''


if __name__ == '__main__':
    if sys.platform == 'darwin':  # different port if running on MacOsX
        app.run(debug=True, port=8080)
    else:
        app.run(debug=True, port=80)
# start the server with the 'run()' method
