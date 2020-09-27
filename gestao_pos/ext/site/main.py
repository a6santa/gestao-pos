from flask import render_template, flash, redirect, request, url_for, session, flash
from flask import Blueprint
from flask import current_app

bp = Blueprint("site", __name__)

@bp.route("/", methods=['GET'])
def login():
    return 'ok'