from flask import render_template, flash, url_for, redirect, request
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.urls import url_parse

from app import app, db, login_manager
from app.models.forms import LoginForm, UserForm
from app.models.tables import User


@login_manager.user_loader
def load_user(id):
    return User.query.filter_by(id=id).first()


@app.route("/index")
@app.route("/")
def index():
    return render_template('index.html')


@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect('admin')
    else:
        form = LoginForm()
        if form.validate_on_submit():
            user = User.query.filter_by(username=form.username.data).first()
            if user and user.password == form.password.data:
                print(form.remember_me.data)
                login_user(user)
                next_page = request.args.get('next')
                if not next_page or url_parse(next_page).netloc != '':
                    next_page = url_for('admin')
                return redirect(next_page)
            else:
                flash("Usuário ou senha invalida")

        return render_template('login.html', form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route("/admin")
@login_required
def admin():
    return render_template('admin.html')


@app.route("/user", methods=['GET', 'POST'])
@login_required
def cad_user():
    users = User.query.all()
    form_cad = UserForm()

    if form_cad.validate_on_submit():
        if form_cad.username.data in [user.username for user in users]:
            flash('Usuário já existe')
        elif form_cad.email.data in [user.email for user in users]:
            flash('email já existe')
        elif form_cad.password.data != form_cad.confirm_password.data:
            flash('Senha invalida')
        else:
            user = User(username=form_cad.username.data, password=form_cad.password.data,
                        name=form_cad.name.data, email=form_cad.email.data)
            db.session.add(user)
            db.session.commit()
            flash('Usuário cadastrado com sucesso')

        return redirect(url_for('cad_user'))

    return render_template('user.html', form_cad=form_cad, users=users)
