from os import environ


class Config:
    # ProjetName_MicroserviceName_VariableName
    ENV = environ.get("SKOB_AUTHZ_ENV", "production")

    DEBUG = int(environ.get("SKOB_AUTHZ_DEBUG", "0"))

    TESTING = int(environ.get("SKOB_AUTHZ_TESTING", "0"))
