import os

from flask import Flask, session
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)

# Check for environment variable
if not os.getenv("postgres://dfbfzhxttjceom:edea8aaa8a670b3a76ecc2aae51cc8134e97a1f37398cbf3cfbc04fb189ffb68@ec2-54-246-90-10.eu-west-1.compute.amazonaws.com:5432/d6bhhs6dliagvb"):
    raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Set up database
engine = create_engine(os.getenv("postgres://dfbfzhxttjceom:edea8aaa8a670b3a76ecc2aae51cc8134e97a1f37398cbf3cfbc04fb189ffb68@ec2-54-246-90-10.eu-west-1.compute.amazonaws.com:5432/d6bhhs6dliagvb"))
db = scoped_session(sessionmaker(bind=engine))


@app.route("/")
def index():
    return "Project 1: TODO"
