from flask import Flask
from requests import request
app=Flask(__name__)

# Routing is mechanism through whcih it is decided
#which function will run for which url

#We do this using app.route() Decorator

@app.route('/welcome' , method=['GET' , 'POST'])
def  welcome_page():
    if request.method == 'POST':
        return "Heyyyyy"


app.run(debug = True)
'''
Interally flaks uses a library called as werkexueg through which
it handle all the mappings/http/wsgi plumbing
so flask stays simple;

# When any URl is called python dispatches function based on mapping in the map;

'''

#Dynamic Routes with convertors
@app.route('/user/<username>')          # default type: string
def show_user(username):
    return f"User: {username}"

@app.route('/post/<int:post_id>')       # must be an integer
def show_post(post_id):
    return f"Post ID: {post_id}"

@app.route('/price/<float:amount>')     # must be a float
def show_price(amount):
    return f"Amount: {amount}"

@app.route('/files/<path:subpath>')     # accepts slashes too, e.g. "a/b/c"
def show_file(subpath):
    return f"Path: {subpath}"


#Request methods
'''
By default route reponds to the GET only;
# But we can explicitly tell that which methods it also can accept;

if request method is other than declared methods
python server will automatically rejects that
'''

# Subdomains
app.config['SERVER_NAME'] = 'example.com'

@app.route('/', subdomain='api')
def api_home():
    return "API root"

@app.route('/', subdomain='www')
def www_home():
    return "Main site"