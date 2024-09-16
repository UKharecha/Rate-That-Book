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

    def token_auth(self, endpoint=""):
        def inner1(func):
            @wraps(
                func
            )  # In user Controller we can use auth_token for more routes or else it will try to overwrite in every routes.
            def inner2(*args):
                endpoint = request.url_rule
                print(endpoint)
                authorization = request.headers.get("authorization")
                if re.match("^Bearer *([^ ]+) *$", authorization, flags=0):
                    token = authorization.split(" ")[1]
                    try:
                        jwtdecoded = jwt.decode(token, "umang", algorithms="HS256")
                    except:
                        return make_response({"ERROR": "TOKEN_EXPIRED"}, 401)
                    role_id = jwtdecoded["payload"]["role_id"]
                    self.cur.execute(
                        f"SELECT roles FROM accessibility_view WHERE endpoint = '{endpoint}'"
                    )
                    result = self.cur.fetchall()
                    if len(result) > 0:
                        allowed_roles = json.loads(result[0]["roles"])
                        if role_id in allowed_roles:
                            return func(*args)
                        else:
                            return make_response({"ERROR": "INVALID_ROLE"}, 404)
                    else:
                        return make_response({"ERROR": "UNKNOWN_ENDPOINT"}, 404)

                else:
                    return make_response({"ERROR": "INVALID TOKEN"}, 401)

            return inner2

        return inner1
