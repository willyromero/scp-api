from flask import current_app


def int_or_none(value):
    try:
        if value.lower() == "none":
            return None
        number = int(value)
        return number
    except:
        return value


def check_permission(key):
    
    try:
        if current_app.config.get("SECRET_KEY") == key:
            return True
        else:
            return False
    except:
        return False
