from flask import request
from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    data = { 'ip': request.access_route[0], 'user_agent': request.user_agent.string }
    return render_template("index.html", data = data)

@app.route('/ip')
def ip():
    return request.access_route[0]

@app.route('/user-agent')
def userAgent():
    return request.user_agent.string

@app.route('/test')
def test():
    route = ""
    for item in request.access_route:
        route = route + item + "\n"
    return route
