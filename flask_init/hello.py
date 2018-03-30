from flask import Flask, url_for, render_template
# unique name for Flask class instance
app = Flask(__name__)

"""
# decorator
@app.route('/login', methods = ['GET'])
def login():
    return '<form methods="get" action="/login"><input type="text" name="username" /><p><button type="submit">Submit</button></form>'
"""
@app.route('/hello')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name_template = name)

# create a server to wait for URL to enter, then follow 
# decorator routes to run functions
if __name__ == '__main__':
    app.debug = True
    app.run()
