from os import environ


class Config:
    ########### Global Configuration ###########
    # ProjetName_MicroserviceName_VariableName
    ENV = environ.get("SKOB_AUTHZ_ENV", "production")

    DEBUG = int(environ.get("SKOB_AUTHZ_DEBUG", "0"))

    TESTING = int(environ.get("SKOB_AUTHZ_TESTING", "0"))

    SECRET = environ.get("SKOB_AUTHZ_SECRET", "VERY_HARD_SECURE_SECRET_CODE")

    JWT_ALGO = environ.get("SKOB_AUTHZ_JWT_ALGO", "HS512")

    JWT_TOKEN_LIFETIME = int(environ.get("SKOB_AUTHZ_JWT_TOKEN_LIFETIME", "86400"))

    ########### Database Configurations #######

    SQLALCHEMY_DATABASE_URI = environ.get("SKOB_AUTHZ_DATABASE_URI", None)
    SQLALCHEMY_TRACK_MODIFICATIONS = TESTING

    ########### User Configuration ###########

    USER_DEFAULT_ROLE = environ.get("SKOB_AUTHZ_USER_DEFAULT_ROLE", "member")
    USER_DEFAULT_STATUS = environ.get("SKOB_AUTHZ_USER_DEFAULT_STATUS", "inactive")
