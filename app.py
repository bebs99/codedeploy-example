from markupsafe import escape

@app.route("/")
def hello(home.html):
    return f"Hello, {escape(home.html)}!"
