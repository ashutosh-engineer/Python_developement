'''
Blueprints ar ethe mini flask app that has its own routes , methods etc.
Blueprint wont run untill it is regiistered in the flask app.

#The problem it solves;
1.Git merege conflict avoidance
-Think 2 devs working on a single app.py after pushing git might flag
it as merge conflict , there chnages are logically diffferent but
Might considered as close chnages because of same files

2.It increases readabilty
-Think where 200 routes in an single file

3-Isolation testing
-IF routes are in the Blueprint testing can be done in isolation
'''
from flask import Flask, Blueprint
user_bp=Blueprint('users', __name__)

@user_bp.route('/login')
def login():
    return "Logined"

@user_bp.route('/signup')
def signup():
    return "Signuped"

