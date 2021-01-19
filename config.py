import logging

class Config(object):
    
    FLASK_ADMIN_SWATCH = 'Superhero'
    BOOTSTRAP_BOOTSWATCH_THEME = 'Superhero'
    SECRET_KEY = 'SuperSecretApplicationKey'
    SECURITY_PASSWORD_SALT = ''
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'postgresql://victors:victor77@localhost/victors_blog'

LOGGING = {
    'version': 1,
    'formatters': {
        'default': {
            'format': '[%(asctime)s] - [%(name)s] - [%(levelname)s] - [%(message)s]'
        },
    },
    'handlers': {
        'file': {
            'class': 'logging.FileHandler',
            'formatter': 'default',
            'filename': 'application.log'
        },
    },
    'loggers': {
        'application': {
            'level': logging.DEBUG,
            'handlers': ['file', ]
        },
    },
}