from flask import Markup, flash
from flask_admin.actions import action
from flask_admin.contrib.sqla import ModelView, filters
from wtforms import PasswordField
from werkzeug.security import generate_password_hash
from gestao_pos.ext.db.models import User
from gestao_pos.ext.db import db
from gestao_pos.ext.admin import MyView



class UserAdmin(MyView):
    """Interface admin de user"""
    
    # form_columns = ('email', 'passwd', 'group', 'admin', 'status')
    # form_extra_fields = {
    #     'passwd': PasswordField('Password')
    # }
    # column_list = ["admin", "email", 'group', 'admin', 'status']
    column_searchable_list = ["email"]

    can_edit = True
    can_create = True
    can_delete = True

    @action("toggle_admin", "Toggle admin status", "Are you sure?")
    def toggle_admin_status(self, ids):
        users = User.query.filter(User.id.in_(ids))
        for user in users.all():
            user.admin = not user.admin
        db.session.commit()
        flash(f"{users.count()} usuários alterados com sucesso!", "success")

    def on_model_change(self, form, model, is_created):
        model.passwd = generate_password_hash(model.passwd)