from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions
from werkzeug.security import check_password_hash, generate_password_hash
from helpers import apology, login_required
from data_base import User_Data


# Configure application
app = Flask(__name__)

# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///sport.db")

@app.route("/",methods=["GET", "POST"])
@login_required
def index():
    """TODO"""
    """at this point you should only display the event form the database and return a html page"""
    return "hello user"


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")

@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""
    # make this clean
    # Forget any user_id

    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE email = :username",
                          username=request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    # Forget any user_id
    session.clear()
    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Ensure username was submitted
        if not request.form.get("email"):
            return apology("Missing the E-mail")
        if not request.form.get("username"):
            return apology("Missing the name")
        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password")
        elif not request.form.get("confirmation"):
            return apology("must provide password")
        elif request.form.get("password") != request.form.get("confirmation"):
            return apology("not match")
        # Insert the data of the seller
        username = request.form.get("username")
        password = request.form.get("password")
        email = request.form.get("email")
        hash = generate_password_hash(password)
        dbMan = User_Data()
        print("1")
        # Insert the data of the new user
        newUser = dbMan.create_user(username, hash, email)
        if not newUser:
            return apology("You are Already registered", 400)
       # Remember which user has logged in
        session["id"] = newUser
        # Redirect user to register page
        return redirect("/")
    else:
        return render_template("register.html")


@app.route("/start",methods=["GET", "POST"])
def start():
    if request.method == "POST":
        return redirect("/register")
    return render_template("start.html")

@app.route("/createvent", methods=["GET", "POST"])
@login_required
def createvent():

    """Allow the user to create events from a list"""
    if request.method == "POST":
        eventName = request.form.get("eventname")
        if not eventName:
            return apology("please enter the event name")
        eventDate = request.form.get("eventdate")
        if not eventDate:
            return apology("please enter the event date")
        eventPlace = request.form.get("eventplace")
        if not eventPlace:
            return apology("please enter the event place")
        eventType = request.form.get("eventtype")
        if not eventPlace:
            return apology("please enter the event type")
        dbMann = User_Data()
        newEvent = dbMann.createNewEvent(eventDate, eventPlace, eventType, eventName)
        return redirect("/register")
        print("hello")
    else:
        return render_template("screatevent.html")



"""@app.route("/joinevent", methods=["GET", "POST"])
def joinevent():
    TODO
        allow the user to join the data base
    return"""