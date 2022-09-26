from controllers import person_controller
from flask import Blueprint, current_app, request
from .middlewares import request_validator

main = Blueprint("person", __name__)


@main.route("<ci>")
def get_person_data(ci):
    request_key = request.json["user_key"]

    if request_validator.check_permission(request_key):
        timeout = request_validator.int_or_none(
            current_app.config["DEFAULT_TIMEOUT"])

        if (timeout == None or isinstance(timeout, int)):
            person_data = person_controller.get_person_data(
                ci, to=timeout)
        else:
            return {"status": "FAILED", "data": {"error": "Default timeout must be number or None value"}}
        
        return person_data
    else:
        return {"status": "FAILED", "data": {"error": "You can't use this endpoint, unauthorized"}}


@main.route("<ci>/<to>")
def get_person_data_timeout(ci, to):
    request_key = request.json["user_key"]

    if (request_validator.check_permission(request_key)):
        timeout = request_validator.int_or_none(to)

        if (timeout == None or isinstance(timeout, int)):
            person_data = person_controller.get_person_data(
                ci, to=timeout)
        else:
            return {"status": "FAILED", "data": {"error": "Timeout param must be number or None value"}}
        
        return person_data
    else:
        return {"status": "FAILED", "data": {"error": "You can't use this endpoint, unauthorized"}}


@main.errorhandler(500)
def bad_request():
    return {"status": "FAILED", "data": {"error": "Bad request"}}, 500
