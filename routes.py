from app import app
from flask import render_template
from database import db

@app.route("/")
def index():
    return render_template("frontpage.html")

@app.route("/contributor/<name>")
def contr(name):
    sql = "SELECT r.name from releases r, personnel p WHERE p.name=:name and p.release_id IS r.id"
    personnel = db.session.execute(sql, {"name":name})
    return render_template("contributor.html").fetchall

@app.route("/result", methods=["POST"])
def result():
    #sql todo
    return render_template("result.html", name=request.form["search"])

@app.route("/release/<name>")
def release(name):
    sql = "SELECT name from releases WHERE name=:name"
    personnel = db.session.execute(sql, {"name":name})
    return render_template("contributor.html")


@app.route("/artist/<name>")
def artist(name):
    sql = "SELECT name from releases WHERE performer=:name"
    releases = db.session.execute(sql, {"name":name})
    
    return render_template("artist.html", artist=name, releases=releases.fetchall())