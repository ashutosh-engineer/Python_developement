# Web server Gateway Inteface
'''
In Earliest time if you have to make an python web application
for everyother framework you have to write Some different messy
code there were no common standards for that;

For this, WSGI is developed an common Webserver GAteway
For all the frameworks django , flask ,anythinh
'''

# How flask fit in that
from flask import Flask

app=Flask(__name__)
# This app varibale is also an WSGI application 

# Server role(Gunicorn)
'''
In local testing what we do is we easily run
with app.run() that is own small wsgi server instance which runs
Locally;

But this is Enefficient it handle to much less requests
for this Gunicorn is used in this
'''


#Gunicorn
'''
Guniocorn start with multiple workers;
MAybe 5 workers

Every worker handle their request at their place only
if every worker is busy then request will wait in 
Queue untill any worker doesntGet freed;
'''

# debug = True
'''
In this deubug=True if any error comes then 
An interractie console will be opened in the browser
Showing the Errors;
'''
