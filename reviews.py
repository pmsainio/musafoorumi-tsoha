from flask import render_template, request, redirect, session
from database import db

def comment(name):
    comment = request.form["comment"]
    if comment == "":
        return render_template("release.html", error="Kirjoitathan ensin jotain.")
    else:    
        release_id = db.session.execute("SELECT id FROM releases WHERE name=:name", {"name":name}).fetchone()[0]
        username = session.get("username")
        commenter_id = db.session.execute("SELECT id FROM Users WHERE name=:username", {"username":username}).fetchone()[0]
        sql = "INSERT INTO Comments (comment, release_id, commenter_id, timestamp) VALUES (:comment, :release_id, :commenter_id, NOW())"
        db.session.execute(sql, {"comment":comment, "release_id":release_id, "commenter_id":commenter_id})
        db.session.commit()
        return redirect("/release/" + name)

def review(name):
    score = request.form["score"]
    reviewee_id = db.session.execute("SELECT id FROM releases WHERE name=:name", {"name":name}).fetchone()[0]
    username = session.get("username")
    reviewer_id = db.session.execute("SELECT id FROM Users WHERE name=:username", {"username":username}).fetchone()[0]
    sql = "INSERT INTO Reviews(reviewer_id, reviewee_id, score) VALUES (:reviewer_id, :reviewee_id, :commenter_id)"
    db.session.execute(sql, {"reviewer_id":reviewer_id, "reviewee_id":reviewee_id, "score":score})
    db.session.commit()
    return redirect("/release/" + name)