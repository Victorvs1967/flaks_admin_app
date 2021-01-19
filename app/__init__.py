import logging
from logging.config import dictConfig
from flask_bootstrap import Bootstrap
from flask import Flask

from config import Config, LOGGING


def create_app():

    dictConfig(LOGGING)

    app = Flask(__name__)
    app.logger = logging.getLogger('application')
    app.logger.info('Application started')

    app.config.from_object(Config())

    return app

app = create_app()
bootstrap = Bootstrap(app)

from app import admin, views, models