from werkzeug.security import check_password_hash, generate_password_hash
from flask import render_template, request, redirect, session
from database import db
import secrets

def create_user():
    username = request.form["username"]
    sql = "SELECT name, password FROM users WHERE name=:name"
    result = db.session.execute(sql, {"name":username})
    user = result.fetchone()    
    if not user:
        password1 = request.form["password1"]
        password2 = request.form["password2"]
        if username == "":
            return render_template("register.html", error="Valitse käyttäjänimi.")
        if len(username) > 20:
            return render_template("register.html", error="Valitse lyhyempi käyttäjänimi.")
        if password1 != password2:
            return render_template("register.html", error="Salasanat eivät täsmää.")
        if len(password1) < 8:
            return render_template("register.html", error="Salasanan on oltava vähintään kahdeksan merkkiä pitkä.")
        hash_value = generate_password_hash(password1)
        sql = "INSERT INTO Users (name, password) VALUES (:username, :password)"
        db.session.execute(sql, {"username":username, "password":hash_value})
        db.session.commit()
        session["username"] = username
        return redirect("/")
    else:
        return render_template("register.html", error="Käyttäjänimi on varattu.")

def login(name, password):
    sql = "SELECT name, password FROM users WHERE name=:name"
    result = db.session.execute(sql, {"name":name})
    user = result.fetchone()
    if not user:
        return render_template("login.html", error="Käyttäjää ei löydy.")
    else:
        if check_password_hash(user.password, password):
            session["username"] = name
            session["csrf_token"] = secrets.token_hex(16)
            return redirect("/")
        else:
            return render_template("login.html", error="väärä käyttäjätunnus tai salasana")