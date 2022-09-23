from controllers import person_controller
from flask import Blueprint, current_app
from .middlewares import request_validator

main = Blueprint("person", __name__)


@main.route("<ci>/<pw>")
def get_person_data(ci, pw):
    if (request_validator.password(pw)):
        timeout = request_validator.int_or_none(current_app.config["DEFAULT_TIMEOUT"])

        if (timeout == None or isinstance(timeout, int)):
            person_data = person_controller.get_person_data(
                ci, to=timeout)
        else:
            return {"status": "FAILED", "data": {"error": "Default timeout must be number or None value"}}
        return person_data
    else:
        return {"status": "FAILED", "data": {"error": "You cannot use this endpoint, bad request param password"}}


@main.route("<ci>/<pw>/<to>")
def get_person_data_timeout(ci, pw, to):
    if (request_validator.password(pw)):
        timeout = request_validator.int_or_none(to)

        if (timeout == None or isinstance(timeout, int)):
            person_data = person_controller.get_person_data(
                ci, to=timeout)
        else:
            return {"status": "FAILED", "data": {"error": "Timeout param must be number or None value"}}
        return person_data
    else:
        return {"status": "FAILED", "data": {"error": "You cannot use this endpoint, bad request password or timeout"}}


@main.errorhandler(500)
def bad_request():
    return {"status": "FAILED", "data": {"error": "Bad request timeout"}}, 500
