import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required

# Configure application
app = Flask(__name__)

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///users.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/", methods=["GET", "POST"])
def index():
    """Home page"""

    return render_template("index.html")


@app.route("/bikes", methods=["GET"])
def bikes():
    """Product page"""

    return render_template("triumph.html")
    # below is for the version that changes the single page content with JavaScript
    # return render_template("bikes.html")


@app.route("/triumph", methods=["GET"])
def triumph():
    """Product page"""

    return render_template("triumph.html")


@app.route("/ktm", methods=["GET"])
def ktm():
    """Product page"""

    return render_template("ktm.html")


@app.route("/mvagusta", methods=["GET"])
def mvagusta():
    """Product page"""

    return render_template("mvagusta.html")


@app.route("/ducati", methods=["GET"])
def ducati():
    """Product page"""

    return render_template("ducati.html")


@app.route("/about", methods=["GET"])
def about():
    """Staff page"""

    return render_template("dealer.html")
    # below is for the version that changes the single page content with JavaScript
    # return render_template("about.html")


@app.route("/dealer", methods=["GET"])
def dealer():
    """Staff page"""

    return render_template("dealer.html")


@app.route("/sales", methods=["GET"])
def sales():
    """Staff page"""

    return render_template("sales.html")


@app.route("/finance", methods=["GET"])
def finance():
    """Staff page"""

    return render_template("finance.html")


@app.route("/workshop", methods=["GET"])
def workshop():
    """Staff page"""

    return render_template("workshop.html")


@app.route("/contact", methods=["GET"])
def contact():
    """Contact page"""

    return render_template("contact.html")


@app.route("/contact_form", methods=["POST"])
def contact_form():
    """Contact form"""

    # Ensure user input is correct
    contact_name = request.form.get("contact-name")
    if not contact_name:
        return apology("must provide contact name", 400)
    contact_email = request.form.get("contact-email")
    if not contact_email:
        return apology("must provide email address", 400)
    contact_message = request.form.get("contact-message")
    if not contact_message:
        return apology("must provide message", 400)

    # Update contact table
    db.execute(
        "INSERT INTO contact (id, contact_name, contact_email, contact_message) VALUES (?, ?, ?)",
        contact_name,
        contact_email,
        contact_message,
    )

    # Redirect user to home page
    return redirect("/")


@app.route("/newsletter", methods=["POST"])
def newsletter():
    """Register form"""

    # Ensure user input is correct
    newsletter_email = request.form.get("newsletter-email")
    if not newsletter_email:
        return apology("must provide email address", 400)

    # Query database for user's name
    check_email = db.execute(
        "SELECT newsletter_email FROM users WHERE newsletter_email = ?",
        newsletter_email,
    )

    # If email address already in newsletter table
    if check_email != 0:
        return apology("email address already subscribed", 400)
    # Otherwise email address not in newsletter table
    else:
        # Update newsletter table
        db.execute(
            "INSERT INTO newsletter (id, newsletter_email) VALUES (?)", newsletter_email
        )

        flash("Thank you for subscribing")


@app.route("/regilog", methods=["GET"])
def regilog():
    """Register and log in page"""

    return render_template("regilog.html")


@app.route("/register", methods=["POST"])
def register():
    """Register user"""

    # Clear user id
    session.clear()

    # Ensure username was submitted
    register_name = request.form.get("register-name")
    if not register_name:
        return apology("must provide user name", 400)

    # Ensure password was submitted
    register_password = request.form.get("register-password")
    if not register_password:
        return apology("must provide password", 400)

    # Ensure password confirmation was submitted
    confirmation = request.form.get("confirm")
    if not confirmation:
        return apology("must provide confirmation", 400)

    # Ensure password matches password confirmation
    if register_password != confirmation:
        return apology("passwords must match", 400)

    # Query database for user name
    rows = db.execute("SELECT * FROM user WHERE user_name = ?", register_name)

    # Ensure user name not in use
    if len(rows) != 0:
        return apology("user name in use", 400)
    else:
        # Hash password
        password_hash = generate_password_hash(register_password)

        # Add user to database
        db.execute(
            "INSERT INTO user (user_name, password_hash) VALUES(?, ?)",
            register_name,
            password_hash,
        )

        flash("Thanks for registering. Please log in.")

        # Redirect user to regilog route
        return redirect("/regilog")


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Clear user_id
    session.clear()

    # Ensure username was submitted
    user_name = request.form.get("user-name")
    if not user_name:
        return apology("must provide user name", 400)

    # Ensure password was submitted
    login_password = request.form.get("login-password")
    if not login_password:
        return apology("must provide password", 400)

    # Query database for username
    rows = db.execute("SELECT * FROM user WHERE user_name = ?", user_name)

    # Ensure username exists
    if len(rows) != 1:
        return apology("invalid user name", 400)

    # Ensure password is correct
    if not check_password_hash(rows[0]["password_hash"], login_password):
        return apology("invalid password", 400)

    # Remember which user has logged in
    session["user_id"] = rows[0]["id"]

    # Redirect user to blog route
    return redirect("/blog")


@app.route("/blog", methods=["GET", "POST"])
@login_required
def blog():
    """Table of blog posts"""

    # Query database for user's name
    name = db.execute("SELECT user_name FROM user WHERE id = ?", session["user_id"])[0][
        "user_name"
    ]

    # Query database for blogs
    blogs = db.execute("SELECT * FROM blog ORDER BY timestamp DESC")

    # Output to user
    return render_template("blog.html", name=name, blogs=blogs)


@app.route("/blog_post", methods=["GET", "POST"])
@login_required
def blog_post():
    """Create new post"""

    # Query database for user's name
    blog_user = db.execute(
        "SELECT user_name FROM user WHERE id = ?", session["user_id"]
    )[0]["user_name"]

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        blog_title = request.form.get("blog-title")
        if not blog_title:
            return apology("must provide title", 400)
        content = request.form.get("content")
        if not content:
            return apology("must provide content", 400)

        db.execute(
            "INSERT INTO blog (blog_title, blog_user, content, replies, likes) VALUES (?, ?, ?, ?, ?)",
            blog_title,
            blog_user,
            content,
            0,
            0,
        )

        return redirect("/blog")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("blog-post.html", blog_user=blog_user)


@app.route("/blog_select", methods=["GET", "POST"])
@login_required
def blog_select():
    """Interact with selected post"""

    # Query database for user's name
    blog_user = db.execute(
        "SELECT user_name FROM user WHERE id = ?", session["user_id"]
    )[0]["user_name"]

    data = request.form.get("data")
    fields = db.execute("SELECT * FROM blog WHERE id = ?", data)
    return render_template("blog-select.html", blog_user=blog_user, fields=fields)


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)