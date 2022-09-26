from flask import Flask
from routes import not_found, person


app = Flask(__name__)

if __name__ == "__main__":

    app.config.from_object("config.ProductionConfig")
    # app.config.from_object("config.DevelopmentConfig")

    # Blueprints
    app.register_blueprint(person.main, url_prefix="/scp/api")

    # error page
    app.register_error_handler(404, not_found.page)

    app.run()
