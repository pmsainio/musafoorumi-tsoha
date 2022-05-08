from app import app
from flask import render_template, request, redirect, session
from database import db
from os import getenv
import users
import releases

app.secret_key = getenv("SECRET_KEY")

@app.route("/")
def index():
    sql = "SELECT name, performer, year FROM Releases ORDER BY year"
    releases = db.session.execute(sql)
    sql = "SELECT performer FROM Releases"
    artists = db.session.execute(sql)
    return render_template("frontpage.html", releases=releases, artists=artists)

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    if request.method == "POST":
        name = request.form["username"]
        password = request.form["password"]
        return users.login(name, password)

@app.route("/logout")
def logout():
    del session["username"]
    return redirect("/")

@app.route("/register",methods=["GET", "POST"])
def signup():
    if request.method == "GET":
        return render_template("register.html")
    if request.method == "POST":
        return users.create_user()
        

@app.route("/result", methods=["GET"])
def result():
    search = request.args["search"]
    sql = "SELECT performer, name, year FROM Releases WHERE UPPER(performer) \
            LIKE UPPER(:search) OR UPPER(name) LIKE UPPER(:search) ORDER BY year"
    result = db.session.execute(sql, {"search":"%"+search+"%"})
    results = result.fetchall()
    return render_template("result.html", search=search, results=results)

@app.route("/release/<name>", methods=["GET","POST", "#"])
def release(name):
    if request.method == "GET":
        average = releases.load_average(name)
        score = releases.load_score(name)
        release, tracks, personnel, comments = releases.load_page(name)
        return render_template("release.html", release=name, \
                                                releases=release,\
                                                tracks=tracks, \
                                                personnel=personnel, \
                                                comments=comments, \
                                                average=average, \
                                                score=score)
    if request.method == "POST":
        if session["csrf_token"] != request.form["csrf_token"]:
            return redirect("/release/" + name)
        else:
            return releases.review(name)

@app.route("/artist/<name>")
def artist(name):
    sql = "SELECT name from releases WHERE performer=:name ORDER BY year"
    releases = db.session.execute(sql, {"name":name})
    return render_template("artist.html", artist=name, releases=releases.fetchall())

@app.route("/contributor/<name>")
def contr(name):
    sql = "SELECT r.name, p.role from releases r, personnel p \
            WHERE p.name=:name and p.release_id = r.id"
    personnel = db.session.execute(sql, {"name":name})
    return render_template("contributor.html", person=name, personnel=personnel.fetchall())



