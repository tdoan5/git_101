from flask import Flask
# unique name for Flask class instance
app = Flask(__name__)

# decorator
@app.route('/')
def index():
    return "Index Page"

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return "User %s" % username 

@app.route('/hello')
def hello_world():
    return "Hello World!"

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return "Post %d" % post_id

# create a server to wait for URL to enter, then follow 
# decorator routes to run functions
if __name__ == '__main__':
    app.debug = True
    app.run()
