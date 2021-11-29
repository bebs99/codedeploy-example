from flask import render_template

@app.route('/')
@app.route('/')
def hello(name=None):
    return render_template('home.html', name=name)
