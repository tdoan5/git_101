import os

from flask import Flask, request, render_template
# unique name for Flask class instance
app = Flask(__name__)

# decorator
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return "User %s logged in" % request.form['username']
    return render_template('login.html')

# create a server to wait for URL to enter, then follow 
# decorator routes to run functions
if __name__ == '__main__':
    app.debug = True
    app.run()
