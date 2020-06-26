import os

from flask import Flask, session
from flask import Flask, request, render_template
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)


# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Set up database
engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))

@app.route("/")
def index():
    flights = db.execute("SELECT * FROM flights").fetchall()
    return render_template("index.html", flights=flights)

@app.route("/notepad", methods=["GET","POST"])
def notepad():
    if request.method =="POST":
        note = request.form.get("note")
        session["notes"].append(note)
    if session.get("notes") is None:
        session["notes"]=[]
    return render_template("notepad.html",notes=session["notes"])

@app.route("/book")
def book():
    flights = db.execute("SELECT * FROM flights").fetchall()
    return render_template("book.html",flights=flights)

@app.route("/booked", methods=["POST"])
def booked():
    name = request.form.get("name")
    try:
        flight_id = request.form.get("flight_id")
    except ValueError:
        return render_template("error.html", message="Invalid flight number")
    
    if db.execute("SELECT*FROM flights WHERE id=:id", {"id": flight_id}).rowcount == 0:
        return render_template("error.html", message="No such flight with that id.")
    db.execute("INSERT INTO passengers (name, flight_id) VALUES (:name, :flight_id)", {"name":name,"flight_id":flight_id})
    db.commit()
    return render_template("booked.html")
    