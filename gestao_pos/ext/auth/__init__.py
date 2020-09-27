from gestao_pos.ext.admin import admin as base_admin
from gestao_pos.ext.auth.admin import MyView
from gestao_pos.ext.db.models import User
from gestao_pos.ext.db import db


def init_app(app):

    base_admin.add_view(MyView(User, db.session))