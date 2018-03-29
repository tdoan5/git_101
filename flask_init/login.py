import os

from flask import Flask, request
# unique name for Flask class instance
app = Flask(__name__)

# decorator
@app.route('/login', methods = ["GET", "POST"])
def login():
    if request.method == "POST":
        return 'username is ' + request.values["username"]
    else:
        return '<form methods="POST" action="/login"><input type="text" name="username" /><p><button type="submit">Submit</button></form>'

# create a server to wait for URL to enter, then follow 
# decorator routes to run functions
if __name__ == '__main__':
    app.debug = True
    app.run()
