import logging
from logging.config import dictConfig
from flask_bootstrap import Bootstrap
from flask import Flask

from config import Config, LOGGING

dictConfig(LOGGING)

app = Flask(__name__)
app.logger = logging.getLogger('application')
app.logger.info('Application started')

bootstrap = Bootstrap(app)
app.config.from_object(Config())

from app import admin, views, models
