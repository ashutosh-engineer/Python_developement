# What is an error- Any exception can be called as the error;
# USer trid to viist a page flask with emit erro404 not found;

# When flask gives 404 we can still create our own error page that is called
# as custom error handling.

# Common http methods;
'''
400-BAd request
401-Unauthroised
403-Forbidden
404-Not found
405-Mehthod Not allowed
500 -Internal server error
'''

# Handling error manually
from flask import Flask, request
app=Flask(__name__)

@app.route("/", methods=["GET"])
def welcome():
    return "Welcome to Randysss tutoial"

@app.errorhandler(404)
def d():
    return "Teri maaaa ki chut",404


if __name__ == "__main__":
    app.run(debug=True)