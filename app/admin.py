from flask import Flask, Blueprint
from flask_admin import Admin
from flask_sqlalchemy import SQLAlchemy
from flask_admin.contrib.sqla import ModelView

from .models import db, Role, User, Post, Category, init_login
from app import app


admin = Admin(app, name='myblog', template_mode='bootstrap4')
admin.add_view(ModelView(Role, db.session))
admin.add_view(ModelView(User, db.session))
admin.add_view(ModelView(Post, db.session))
admin.add_view(ModelView(Category, db.session))

init_login()