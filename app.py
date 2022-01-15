from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import login_required

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Activities, Hardness, Duration
activities = ["Bouldern", "Flexibility", "Yoga", "Endurance","Power Endurance", "Hangboard", "Strength & Power",
            "Running", "Bike", "Hiking", "Mountaineering", "Climbing", "Conditioning"]
hardness = ["Easy", "Moderate", "Hard", "Very Hard"]
months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///diary.db")

# Error Messages
def apology(message):
    """message to user due to missing value."""
    return render_template("apology.html", message=message)


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    """Show last 5 trainings of user"""
    user_id = session["user_id"]
    last_logs = db.execute("SELECT id, date, activity, hardness, duration, description FROM history WHERE user_id = ? ORDER BY id DESC LIMIT 5", user_id)
    return render_template("index.html", last_logs=last_logs)



@app.route("/log", methods=["GET", "POST"])
@login_required
def log():
    """Buy shares of stock"""
    if request.method == "POST":
        date = request.form.get("date")
        activity = request.form.get("activity")
        log_hardness = request.form.get("hardness")
        duration = request.form.get("duration")
        description = request.form.get("description")

        if not date:
            return apology("Please enter a date")
        if not duration:
            return apology("Enter a duration!")

        user_id = session["user_id"]

        db.execute("INSERT INTO history (user_id, date, activity, hardness, duration, description) VALUES (?, ?, ?, ?, ?, ?)",
                    user_id, date, activity, log_hardness, duration, description)

        return redirect("/")
    else:
        return render_template("log.html", activities=activities, hardness=hardness)


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    user_id = session["user_id"]
    history = db.execute("SELECT id, date, activity, hardness, duration, description FROM history WHERE user_id = ? ORDER BY id DESC", user_id)

    return render_template("history.html", history=history)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username")

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password")

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password")

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to homepage
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if (request.method == "POST"):
        username = request.form.get('username')
        password = request.form.get('password')
        confirmation = request.form.get('confirmation')

        if not username:
            return apology('Username is required!')
        elif not password:
            return apology('Password is required!')
        elif not confirmation:
            return apology('Password confirmation is required!')

        if password != confirmation:
            return apology('Passwords do not match!')

        hash = generate_password_hash(password)

        try:
            db.execute("INSERT INTO users (username, hash) VALUES (?, ?)", username, hash)
            return redirect("/")
        except:
            return apology("Username has already registered!")
    else:
        return render_template("register.html")


@app.route("/summary")
@login_required
def summary():
    """Per Activities """
    user_id = session["user_id"]
    summary = db.execute("SELECT activity, count(*) AS quantity, SUM(duration) AS totalTime FROM history WHERE user_id = ? GROUP BY activity ORDER BY id DESC", user_id)

    return render_template("summary.html", summary=summary)