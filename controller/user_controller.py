from app import app
from model.user_model import *
from flask import request, send_file
from datetime import datetime

obj = user_model()


@app.route("/user/getall")
def user_getall_controller():
    return obj.user_getall_model()


@app.route("/book/getall")
def book_getall_controller():
    return obj.book_getall_model()


@app.route("/user/addone", methods=["POST"])  # For Creating from Mysql
def user_addone_controller():
    return obj.user_addone_model(request.form)


@app.route("/book/addone", methods=["POST"])  # For Creating from Mysql
def book_addone_controller():
    return obj.book_addone_model(request.form)
