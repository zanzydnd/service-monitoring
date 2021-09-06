import os
import jwt

secret_word = os.environ.get("SECRETWORD")


def jwt_string(string):
    return jwt.encode({"db_password": string}, key=secret_word)
