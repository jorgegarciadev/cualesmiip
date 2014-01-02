# -*- coding: utf-8 -*-

from flask import request, render_template
from app import app
from forms import TextInput
from app.users.webtools import validator, pokeSite

@app.route('/')
@app.route('/index')
def index():
    data = { 'ip': request.access_route[0], 'user_agent': request.user_agent.string }
    return render_template("index.html", data = data, title = u"¿Cuál es mi IP?")

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

# Just for the funnies

@app.route('/isdownorwhat', methods = ['GET', 'POST'])
def isdownorwhat():
    form = TextInput()
    if form.validate_on_submit():
        url = form.url.data
        url = validator(url)
        pene = pokeSite(url[2])
        return pene[0] + ' - ' + pene[1]

    return render_template('isdownorwhat.html', form = form, title = u"¿Está caido o qué?")

