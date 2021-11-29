from markupsafe import escape

@app.route("/")
def hello():
    return f"Hello, {escape(home.html)}!"
