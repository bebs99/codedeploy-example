from flask import render_template

@app.route('/home/')
@app.route('/home/<name>')
def hello(name=None):
    return render_template('home.html', name=name)
