import json
import mysql.connector
from flask import make_response
from datetime import datetime, timedelta
import jwt
from configs.config import dbconfig


class user_model:
    def __init__(self):
        try:
            self.con = mysql.connector.connect(
                host=dbconfig["hostname"],
                user=dbconfig["username"],
                password=dbconfig["password"],
                database=dbconfig["database"],
            )
            self.cur = self.con.cursor(dictionary=True)
            self.con.autocommit = True
            print("Connection Successful")
        except:
            print("Some Error")

    def user_getall_model(self):
        self.cur.execute("SELECT * FROM users")
        result = self.cur.fetchall()
        if len(result) > 0:
            return make_response({"payload": result}, 200)

        else:
            return make_response({"message": "No Data Found"}, 204)

    def book_getall_model(self):
        self.cur.execute("SELECT * FROM books")
        result = self.cur.fetchall()
        if len(result) > 0:
            return make_response({"payload": result}, 200)

        else:
            return make_response({"message": "No Data Found"}, 204)

    def user_addone_model(self, data):
        self.cur.execute(
            f"INSERT INTO users(name, email, phone, role_id, password) VALUES('{data['name']}', '{data['email']}', '{data['phone']}', '{data['role_id']}', '{data['password']}')"
        )
        return make_response({"message": "User Created Successfully"}, 201)

    def book_addone_model(self, data):
        self.cur.execute(
            f"INSERT INTO books(book_title, book_author, user_id) VALUES('{data['book_title']}','{data['book_author']}', '{data['user_id']}')"
        )
        return make_response({"message": "Book Added Successfully"}, 201)

    def book_addreview_model(self, data):  # Update
        self.cur.execute(
            f"INSERT INTO books(review, books_id, users_id) VALUES('{data['review']}', '{data['user_id']}', '{data['book_id']}')"
        )
        return make_response({"message": "Book Added Successfully"}, 201)

    def user_update_model(self, data):
        self.cur.execute(
            f"UPDATE users SET name='{data['name']}', email='{data['email']}', phone='{data['phone']}', role_id='{data['role_id']}', password='{data['password']}' WHERE id={data['id']}"
        )
        if self.cur.rowcount > 0:
            return make_response({"message": "User Updated Successfully"}, 201)
        else:
            return make_response({"message": "Nothing to Update"}, 202)

    def book_update_model(self, data):
        self.cur.execute(
            f"UPDATE books SET book_title='{data['book_title']}', book_author='{data['book_author']}', user_id='{data['user_id']}'  WHERE id={data['id']}"
        )
        if self.cur.rowcount > 0:
            return make_response({"message": "Book Updated Successfully"}, 201)
        else:
            return make_response({"message": "Nothing to Update"}, 202)

    def book_update_review_model(self, data):  # Update
        self.cur.execute(
            f"UPDATE reviews SET book_title='{data['book_title']}', book_author='{data['book_author']}', books_id='{data['bookd_id']}', users_id='{data['users_id']}' WHERE id={data['id']}"
        )
        if self.cur.rowcount > 0:
            return make_response({"message": "Book's Review Updated Successfully"}, 201)
        else:
            return make_response({"message": "Nothing to Update"}, 202)

    def user_delete_model(self, id):
        self.cur.execute(f"DELETE FROM users WHERE id={id}")
        if self.cur.rowcount > 0:
            return make_response({"message": "User Deleted Successfully"}, 200)
        else:
            return make_response({"message": "Nothing to Delete"}, 202)

    def book_delete_model(self, id):
        self.cur.execute(f"DELETE FROM books WHERE id={id}")
        if self.cur.rowcount > 0:
            return make_response({"message": "Book Deleted Successfully"}, 200)
        else:
            return make_response({"message": "Nothing to Delete"}, 202)

    def book_delete_review_model(self, id):
        self.cur.execute(f"DELETE FROM reviews WHERE id={id}")
        if self.cur.rowcount > 0:
            return make_response({"message": "Book Review Deleted Successfully"}, 200)
        else:
            return make_response({"message": "Nothing to Delete"}, 202)

    def user_login_model(self, data):
        self.cur.execute(
            f"SELECT id, name, email, phone, role_id FROM users WHERE email='{data['email']}' and password='{data['password']}'"
        )
        result = self.cur.fetchall()
        userdata = result[0]
        exp_time = datetime.now() + timedelta(minutes=15)
        exp_epoch_time = int(exp_time.timestamp())
        payload = {"payload": userdata, "exp": exp_epoch_time}
        jwtoken = jwt.encode(payload, "umang", algorithm="HS256")
        return make_response({"token": jwtoken}, 200)
