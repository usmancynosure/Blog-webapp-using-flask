from flask import Flask

app=Flask(__name__)

@app.route("/")
def usman():
    return "Hello usman "

app.run(debug=True)