from flask import render_template, request
from flask import Flask

app = Flask(__name__)

@app.route('/')
def greet():
    datoz = {"a": 1, "b":2}
    return render_template("sample_display.html", data=datoz)


app.run(host='localhost', port=8080, debug=True)