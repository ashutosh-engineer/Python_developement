# Request responses
from flask import Flask , request
app=Flask(__name__)

@app.route("/search")
def search():
    name=request.args.get("name")
    age=request.args.get("age")

    return f"{name} and age is {age}"

# http//localhost:5000/search?name=Ashutsoh&age=19
'''
it can be done directly without using the
.get but if without get any particular args value not passed
then it wil  give error

Whereas through .get if value is not passed it will return none
None

Every value is  intially string
when we pass age=19 then it is Age:"19" not integer 19
'''

# Multiple Queery Parameters in request.args
@app.route("/products")
def products():
    category = request.args.get("category")
    price = request.args.get("price", type=int)
    brand = request.args.get("brand")

    return f"{category} {price} {brand}"


# Request.form is used to in python flaks to get the data send by the Html forms
