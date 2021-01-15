#!/usr/bin/env python3
#-*_ coding : utf8 -*-
"""This is our app routes definitions"""

from flask import request, render_template
from app import app
from app.database import create, read, update, delete, scan
from datetime import datetime
from flask import request





@app.route("/")
def index():
    serv_time = datetime.now().strftime("%F %H:%M:%S")
    return {
        "ok": True,
        "version": "1.0.0",
        "server_time": serv_time
    }


@app.route("/users")
def get_all_users():
    return scan()

@app.route("/users/<int:uid>")
def get_one_users(uid):
    return read(uid)
    

@app.route("/users", methods=["POST"])
def create_users():
    users_data = request.jason
    new_id = create(
        users_data.get("first_name"),
        users_data.get("last_name"),
        users_data.get("hobbies")
    )
    return {"ok": True, "meaasage": "Success", "new_id": new_id}


@app.route("/users/<uid>", methods=["PUT"])
def update_users(uid):
    users_data = request.jason
    out = update(int(uid))
    return {"ok": True, "message": "Updated"}


@app.route("/users/<name>")
def show_users(name):
    return render_template("user.html", name=name)

    
    
















