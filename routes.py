from app import app
from flask import render_template, request, redirect, session
from database import db
from os import getenv
from werkzeug.security import check_password_hash, generate_password_hash

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
        sql = "SELECT name, password FROM users WHERE name=:name"
        result = db.session.execute(sql, {"name":name})
        user = result.fetchone()    
        if not user:
            return redirect("/")           
        else:
            if check_password_hash(user.password, password):
                session["username"] = name
                return redirect("/")
            else:
                return redirect("/")
                


@app.route("/logout")
def logout():
    del session["username"]
    return redirect("/")

@app.route("/register",methods=["GET", "POST"])
def signup():
    if request.method == "GET":
        return render_template("register.html")
    if request.method == "POST":
        username = request.form["username"]
        sql = "SELECT name, password FROM users WHERE name=:name"
        result = db.session.execute(sql, {"name":username})
        user = result.fetchone()    
        if not user:
            password1 = request.form["password1"]
            password2 = request.form["password2"]
            if password1 != password2:
                return redirect("/")
            hash_value = generate_password_hash(password1)
            sql = "INSERT INTO Users (name, password) VALUES (:username, :password)"
            db.session.execute(sql, {"username":username, "password":hash_value})
            db.session.commit()
            session["username"] = username
            return redirect("/")
        else:
            return redirect("/")
        

@app.route("/result", methods=["GET"])
def result():
    search = request.args["search"]
    sql = "SELECT performer, name, year FROM Releases WHERE UPPER(performer) LIKE UPPER(:search) OR UPPER(name) LIKE UPPER(:search) ORDER BY year"
    result = db.session.execute(sql, {"search":"%"+search+"%"})
    results = result.fetchall()
    return render_template("result.html", search=search, results=results)

@app.route("/release/<name>", methods=["GET","POST"])
def release(name):
    if request.method == "GET":
        sql = "SELECT name, performer FROM releases r WHERE r.name=:name"
        releases = db.session.execute(sql, {"name":name})
        sql = "SELECT t.listing, t.name FROM releases r, tracks t WHERE t.release_id = r.id AND r.name=:name"
        tracks = db.session.execute(sql, {"name":name})
        sql = "SELECT p.name, p.role FROM releases r, personnel p WHERE p.release_id = r.id AND r.name=:name"
        personnel = db.session.execute(sql, {"name":name})
        sql = "SELECT c.comment, u.name FROM Comments c, Releases r, Users u WHERE c.release_id = r.id AND u.id = c.commenter_id AND r.name=:name ORDER BY c.timestamp"
        comments = db.session.execute(sql, {"name":name})
        return render_template("release.html", release=name, releases=releases.fetchall(), tracks=tracks.fetchall(), personnel=personnel.fetchall(), comments=comments.fetchall())


    if request.method == "POST":
        comment = request.form["comment"]
        release_id = db.session.execute("SELECT id FROM releases WHERE name=:name", {"name":name}).fetchone()[0]
        username = session.get("username")
        commenter_id = db.session.execute("SELECT id FROM Users WHERE name=:username", {"username":username}).fetchone()[0]
        sql = "INSERT INTO Comments (comment, release_id, commenter_id, timestamp) VALUES (:comment, :release_id, :commenter_id, NOW())"
        db.session.execute(sql, {"comment":comment, "release_id":release_id, "commenter_id":commenter_id})
        db.session.commit()
        return redirect("/release/" + name)

@app.route("/artist/<name>")
def artist(name):
    sql = "SELECT name from releases WHERE performer=:name ORDER BY year"
    releases = db.session.execute(sql, {"name":name})
    return render_template("artist.html", artist=name, releases=releases.fetchall())

@app.route("/contributor/<name>")
def contr(name):
    sql = "SELECT r.name, p.role from releases r, personnel p WHERE p.name=:name and p.release_id = r.id"
    personnel = db.session.execute(sql, {"name":name})
    return render_template("contributor.html", person=name, personnel=personnel.fetchall())



