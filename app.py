from markupsafe import escape

@app.route("/")
def hello(home):
    return f"Hello, {escape(home)}!"
