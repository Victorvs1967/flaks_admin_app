import logging
from flask import Flask, render_template, flash, request, redirect, url_for
import flask_login as login

from app import app


logger = logging.getLogger('application')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/logout')
def logout():
    login.logout_user()
    logger.info('logout successfully')
    return redirect(url_for('index'))
