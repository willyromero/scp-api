from flask import current_app


def int_or_none(value):
    try:
        if value.lower() == "none":
            return None
        number = int(value)
        return number
    except:
        return value


def password(pas):
    try:
        return True if pas == current_app.config["SECRET_KEY"] else False
    except:
        return False
