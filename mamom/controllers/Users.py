from flask import session, render_template, redirect

from mamom import app

@app.route("/mamom/login/", methods=["GET"])
def index_login():
    if "_id" in session:
        return redirect("/mamom/")
    else:
        return render_template("login/login.html")


@app.route("/mamom/signup/", methods=["GET"])
def index_signup():
    if "_id" in session:
        return redirect("/mamom/")
    else:
        return render_template("signup/signup.html")