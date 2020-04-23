from bottle import route, run, template, request

@route('/hello/<name>')
def my_name(name):
    return template('<b>Hello {{name}}</b>!', name=name)


@route('/hello/<name>/json')
def my_name_in_json(name):
    return {"name": name, "greeting": f"Hello {name}!"}


@route('/')
def greet():
    return template("sample_form.html")


@route('/display')
def greet():
    return template("display.html", my_title="asdf", data="my data", other_data=None)


@route('/get_taco')
def my_taco():
    request

@route('/say_hi',method='POST')
def my_name_as_post():
    name = request.forms.get("name")
    # cursor.execute("SELECT ")
    return {"name": name, "greeting": f"Hello {name}!"}



run(host='localhost', port=8080)