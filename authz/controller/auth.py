from flask import abort, request
from jwt import encode
from time import time

from authz import db
from authz.config import Config
from authz.model import User
from authz.schema import UserSchema
from authz.utils import now


class AuthTokenController:
    def create_token():
        if request.content_type != 'application/json':
            abort(415)  # bad media type
        user_schema = UserSchema(only=["username", "password"])
        try:
            data = user_schema.load(request.get_json())  # validate request data
        except:
            abort(400)
        if not data["username"] or not data["password"]:
            abort(400)
        try:
            user = User.query.filter_by(username=data["username"]).first()  # select user
        except:
            abort(500)  # Database Error
        if user is None:
            abort(404)  # user not found

        if user.password != data["password"]:
            user.last_failed_at = now()
            try:
                db.session.commit()
            except:
                sb.session.rollback()
            abort(403)  # incorrect password
        # create New jwt token
        current_time = time()
        try:
            jwt_token = encode(
                {
                    "nbf": current_time,
                    "exp": current_time + Config.JWT_TOKEN_LIFETIME,
                    "user": {
                        "id": user.id,
                        "username": user.username,
                        "role": user.role,
                    }
                },
                Config.SECRET,
                algorithm=Config.JWT_ALGO
            )
        except:
            abort(500)  # JWT encode error

        user_schema = UserSchema()
        return {
            "user": user_schema.dump(user)
        }, 201, {"X-Subject-Token": jwt_token}  # jwt_token.decode("utf8")
