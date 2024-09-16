import json
import mysql.connector
from flask import make_response, request
import jwt
import re
from functools import wraps
from configs.config import *


class auth_model:
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
