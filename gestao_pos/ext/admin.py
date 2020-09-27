from flask import redirect, url_for
from flask_admin import Admin, AdminIndexView
from flask_admin.contrib.sqla import ModelView
from gestao_pos.ext.db import db
from gestao_pos.ext.db.models import User, Terminal, TerminalMovement, TerminalState, TerminalType, Supplier, Supply, SupplyMovement, Customer


class MyView(ModelView):
    can_set_page_size=True
  

admin = Admin()

def init_app(app):

    admin.name = app.config.get("ADMIN_NAME", "Gestão Pos")
    admin.template_mode = app.config.get("TEMPLATE_MODE", "bootstrap3")
    admin.init_app(app)

    admin.add_view(MyView(Terminal, db.session))
    admin.add_view(MyView(TerminalMovement, db.session))
    admin.add_view(MyView(TerminalState, db.session))
    admin.add_view(MyView(TerminalMovement, db.session))
    admin.add_view(MyView(TerminalType, db.session))
    admin.add_view(MyView(Supplier, db.session))
    admin.add_view(MyView(Supply, db.session))
    admin.add_view(MyView(SupplyMovement, db.session))
    admin.add_view(MyView(Customer, db.session))