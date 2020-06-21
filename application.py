import os

from flask import Flask, render_template, request

@app.route("/")
def index():
    title = "Welcome to the book store"
    return render_template("index.html", title = title,)

@app.route("/hello", methods=["GET","POST"])
def hello():
    if request.method == "GET":
        return "Please submit the form instead."
    else:
        name = request.form.get("name");
        return render_template("hello.html", name = name)

#@app.route("/notepad", methods=["GET", "POST"])
#def notepad():
#    if "notes" in session:
#        session["notes"] = []
#    if request.method == "POST":
#        note = request.form.get("note")
#        session["notes"].append(note)
#    return render_template("notepad.html", notes = session["notes"])

#@app.route("/<string:name>")
#def welcome(name):
#    name = name.capitalize();
#    return f"Hi, {name}!"