import os
import datetime

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")


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
    """Show portfolio of stocks"""

    
    return apology("TODO")


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""

    # If the user has reached the route POST
    if request.method == "POST":
        symbol = request.form.get("symbol")
        shares = request.form.get("shares")

        # Check if the symbol is blank
        if not symbol:
            return apology("Please enter a symbol")

        # Check the user input a number of shares
        if not shares:
            return apology("Please input a number of shares")

        # Determine the stock the symbol belongs to
        stock = lookup(symbol)

        # Check if the stock exsists
        if stock == None:
            return apology("This symbol does not exsist")

        # Determine how much cash the user has avaliable
        cash = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])

        # Check the user can afford to buy these shares
        cash_spent = stock["price"] * int(shares)
        if cash_spent > cash[0]["cash"]:
            return apology("Unfortunately, you do not have the funds to buy these stocks")

        # Add the purchase to the table
        db.execute("INSERT INTO purchases (user_id, symbol, price, purchase_time, total) VALUES (?, ?, ?, ?)",
                   session["user_id"], symbol, stock["price"], datetime.datetime.now(), cash_spent)

        # Determine the new value of cash for the user
        cash[0]["cash"] = cash[0]["cash"] - cash_spent
        db.execute("UPDATE users SET cash = ? WHERE id = ?", cash[0]["cash"], session["user_id"])

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("buy.html")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    return apology("TODO")


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

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
        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        )

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(
            rows[0]["hash"], request.form.get("password")
        ):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
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


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""

    # If the user has reached the route POST
    if request.method == "POST":
        symbol = request.form.get("symbol")

        # Check if the symbol is blank
        if not symbol:
            return apology("Please enter a symbol")

        stock = lookup(symbol)

        if (stock == None):
            return apology("This symbol does not exsist")

        return render_template("quoted.html", stock=stock)

    # User reached route via GET (as by clicking a link or via redirect)
    else:
       return render_template("quote.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""

    # If the user has reached the route POST
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        # Check if the username is blank
        if not username:
            return apology("Please enter a username")

        # Check if the password is blank
        if not password:
            return apology("Please enter a password")

        # Check if the confirmation is blank
        if not confirmation:
            return apology("Please enter a confirmation")

        # Check if the password and confirmation match
        if password != confirmation:
            return apology("The passwords do not match")

        # Hash the password
        password_hash = generate_password_hash(password)

        # Check if a username exsists
        existing = db.execute("SELECT * FROM users WHERE username = ?", username)
        if existing:
            return apology("This username already exists")

        # Try the insert the person into the database
        try:
            new_user_id = db.execute("INSERT INTO users (username, hash) VALUES (?, ?)", username, password_hash)

        except (ValueError, sqlite3.IntegrityError):
            return apology("This username already exists")

        # Check in case ValueError wasn't raised
        if not new_user_id:
            return apology("This username already exists")

        # Log in the user automatically
        session["user_id"] = new_user_id

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
       return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    return apology("TODO")
