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
            f"INSERT INTO books(book_title) VALUES('{data['book_title']}')"
        )
        return make_response({"message": "Book Added Successfully"}, 201)
