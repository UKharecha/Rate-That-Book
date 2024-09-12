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


@app.route("/user/addone", methods=["POST"])  # Add User
def user_addone_controller():
    return obj.user_addone_model(request.form)


@app.route("/book/addone", methods=["POST"])  # Add Book
def book_addone_controller():
    return obj.book_addone_model(request.form)


@app.route("/book/review/<id>", methods=["POST"])  # Add Book Review
def book_addreview_controller():
    return obj.book_addreview_model(request.form)


@app.route("/user/update", methods=["PUT"])  # Update User
def user_update_controller():
    return obj.user_update_model(request.form)


@app.route("/book/update", methods=["PUT"])  # Update Book
def book_update_controller():
    return obj.book_update_model(request.form)


@app.route("/user/delete/<id>", methods=["DELETE"])  # Delete User
def user_delete_controller(id):
    return obj.user_delete_model(id)


@app.route("/book/delete/<id>", methods=["DELETE"])  # Delete Book
def book_delete_controller(id):
    return obj.book_delete_model(id)
