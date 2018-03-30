import os

from flask import Flask, request, render_template, redirect, url_for, flash
# unique name for Flask class instance
app = Flask(__name__)

# decorator
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'], request.form['password']):
            flash("Succesfully logged in")
            return redirect(url_for('welcome', username=request.form.get('username'))) 
        else:
            error = "Incorrect username and password"

    return render_template('login.html', error=error)

def valid_login(username, password):
    if username == password:
        return True
    else:
        return False

@app.route('/welcome/<username>')
def welcome(username):
    return render_template('welcome.html', username=username)

# create a server to wait for URL to enter, then follow 
# decorator routes to run functions
if __name__ == '__main__':
    app.debug = True
    app.secret_key = "SuperSecretKey"
    app.run()
