from flask import request, redirect, session
from database import db

def load_page(name):
    sql = "SELECT name, performer FROM Releases r WHERE r.name=:name"
    releases = db.session.execute(sql, {"name":name})
    sql = "SELECT t.listing, t.name FROM Releases r, Tracks t WHERE t.release_id = r.id AND r.name=:name"
    tracks = db.session.execute(sql, {"name":name})
    sql = "SELECT p.name, p.role FROM Releases r, Personnel p WHERE p.release_id = r.id AND r.name=:name"
    personnel = db.session.execute(sql, {"name":name})
    sql = "SELECT c.comment, u.name FROM Comments c, Releases r, Users u \
           WHERE c.release_id = r.id AND u.id = c.commenter_id AND r.name=:name \
           ORDER BY c.timestamp DESC"
    comments = db.session.execute(sql, {"name":name})
    releases, tracks, personnel, comments = releases.fetchall(), \
                                            tracks.fetchall(), \
                                            personnel.fetchall(), \
                                            comments.fetchall()
    return releases, tracks, personnel, comments

def load_average(name):
    sql = "SELECT CAST(AVG(a.score) AS FLOAT) FROM Reviews a, Releases b \
           WHERE a.reviewee_id = b.id AND b.name=:name"
    average = db.session.execute(sql, {"name":name})
    average = average.fetchone()[0]
    if average == None:
        return average
    average = round(average, 2)
    return average

def load_score(name):
    sql = "Select a.score FROM Reviews a, Releases b, Users u \
           WHERE a.reviewer_id = u.id AND a.reviewee_id = b.id AND b.name=:name AND u.name=:username"
    username = session.get("username")
    score = db.session.execute(sql, {"name":name, "username":username})
    score = score.fetchone()
    if score == None:
        return
    return score[0]

def comment(name):
    comment = request.form["comment"]
    if comment == "":
        return
    else:    
        release_id = db.session.execute("SELECT id FROM releases WHERE name=:name", \
                                        {"name":name}).fetchone()[0]
        username = session.get("username")
        commenter_id = db.session.execute("SELECT id FROM Users WHERE name=:username", \
                                         {"username":username}).fetchone()[0]
        sql = "INSERT INTO Comments (comment, release_id, commenter_id, timestamp) \
               VALUES (:comment, :release_id, :commenter_id, NOW())"
        db.session.execute(sql, {"comment":comment, "release_id":release_id, "commenter_id":commenter_id})
        db.session.commit()
        return

def review(name):
    score = request.form["score"]
    comment(name)
    if score == "None":
        return redirect("/release/" + name)
    else:
        username = session.get("username")
        reviewer_id = db.session.execute("SELECT id FROM Users WHERE name=:username", {"username":username}).fetchone()[0]
        review_status = db.session.execute("SELECT a.reviewer_id FROM Reviews a, Releases b \
                                           WHERE b.name=:name AND b.id = a.reviewee_id AND a.reviewer_id=:reviewer_id", \
                                          {"name":name, "reviewer_id":reviewer_id}).fetchone()
        if review_status == None:
            reviewee_id = db.session.execute("SELECT id FROM releases WHERE name=:name", {"name":name}).fetchone()[0]
            sql = "INSERT INTO Reviews(reviewer_id, reviewee_id, score) VALUES (:reviewer_id, :reviewee_id, :score)"
            db.session.execute(sql, {"reviewer_id":reviewer_id, "reviewee_id":reviewee_id, "score":score})
        else:
            sql = "UPDATE Reviews SET score=:score WHERE reviewer_id=:reviewer_id"
            db.session.execute(sql, {"score":score, "reviewer_id":reviewer_id})
        db.session.commit()
        return redirect("/release/" + name)