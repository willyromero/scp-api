from decouple import config


class BaseConfig(object):
    JSON_AS_ASCII = False
    SECRET_KEY = config("SECRET_KEY")
    SCRAP_URL = config("SCRAP_URL")
    DEFAULT_TIMEOUT = config("DEFAULT_TIMEOUT")
    SESSION_COOKIE_DOMAIN = config("SESSION_COOKIE_DOMAIN")


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    SERVER_NAME = config("DEV_SERVER_NAME")


class ProductionConfig(BaseConfig):
    DEBUG = False
    SERVER_NAME = config("SERVER_NAME")
