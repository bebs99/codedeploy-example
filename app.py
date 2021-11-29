from flask import render_template

@app.route('/home/')
@app.route('/home/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)
