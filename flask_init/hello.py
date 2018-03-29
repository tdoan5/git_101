from flask import Flask, url_for
# unique name for Flask class instance
app = Flask(__name__)

# decorator
@app.route('/login', methods = ['GET'])
def login():
    return '<form methods="get" action="/login"><input type="text" name="username" /><p><button type="submit">Submit</button></form>'

# create a server to wait for URL to enter, then follow 
# decorator routes to run functions
if __name__ == '__main__':
    app.debug = True
    app.run()
