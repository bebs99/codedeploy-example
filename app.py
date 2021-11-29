from flask import render_template

@app.route('/hello/')
@app.route('/')
def hello(name=None):
    return render_template('home.html', name=name)
