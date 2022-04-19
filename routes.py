from app import app
from flask import render_template, request, redirect, session
from database import db
from werkzeug.security import check_password_hash, generate_password_hash



@app.route("/")
def index():
    sql = "SELECT name, performer, year FROM Releases ORDER BY year"
    releases = db.session.execute(sql)
    sql = "SELECT performer FROM Releases"
    artists = db.session.execute(sql)
    return render_template("frontpage.html", releases=releases, artists=artists)

@app.route("/result", methods=["GET"])
def result():
    search = request.args["search"]
    sql = "SELECT performer, name, year FROM Releases WHERE UPPER(performer) LIKE UPPER(:search) OR UPPER(name) LIKE UPPER(:search) ORDER BY year"
    result = db.session.execute(sql, {"search":"%"+search+"%"})
    results = result.fetchall()
    return render_template("result.html", search=search, results=results)

@app.route("/release/<name>")
def release(name):
    sql = "SELECT name, performer FROM releases r WHERE r.name=:name"
    releases = db.session.execute(sql, {"name":name})
    sql = "SELECT t.listing, t.name FROM releases r, tracks t WHERE t.release_id = r.id AND r.name=:name"
    tracks = db.session.execute(sql, {"name":name})
    sql = "SELECT p.name, p.role FROM releases r, personnel p WHERE p.release_id = r.id AND r.name=:name"
    personnel = db.session.execute(sql, {"name":name})
    return render_template("release.html", release=name, releases=releases.fetchall(), tracks=tracks.fetchall(), personnel=personnel.fetchall())


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

@app.route("/signup",methods=["POST"])
def signup():
    hash_value = generate_password_hash(password)
    sql = "INSERT INTO users (username, password) VALUES (:username, :password)"
    db.session.execute(sql, {"username":username, "password":hash_value})
    db.session.commit()


@app.route("/login",methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]
    session["username"] = username
    return redirect("/")

@app.route("/logout")
def logout():
    del session["username"]
    return redirect("/")