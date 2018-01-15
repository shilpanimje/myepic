from flask import render_template, request, flash, url_for
from flask_login import login_required
from werkzeug.utils import redirect
from wtforms import Form, BooleanField, StringField, PasswordField, validators

from app import app
from app.logic import user


class LoginForm(Form):
    email = StringField('email', [
        validators.DataRequired()])
    password = PasswordField('New Password', [
        validators.DataRequired(),
        validators.Length(min=8, max=20)
    ])


@app.route('/')
def index():
    return render_template('frontend/index.html')


@app.route('/about')
def about():
    return render_template('frontend/about.html')


@app.route('/adminlogin', methods=['GET', 'POST'])
def admin_login():
    login_form = LoginForm(request.form)

    if request.method == 'POST' and login_form.validate():
        result = user.admin_login(request.form)
        if result == False:
            flash('Username or Password is invalid', 'error')
            return redirect(url_for('admin_login'))
        flash('Logged in successfully')
        return redirect(url_for('dashboard'))

    return render_template('admin/login.html', form=login_form)


@app.route('/adminregister')
def admin_register():
    return render_template('admin/register.html')


@app.route('/adminforgotpass')
def admin_forgot_password():
    return render_template('admin/forgot_password.html')


@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('admin/dashboard.html')


@app.route('/editprofile', methods=['POST', 'GET'])
@login_required
def editprofile():
    if request.method == 'POST':
        user.save_user(request.form)
        return render_template('admin/editprofile.html', data = request.form)
    else:
        return render_template('admin/editprofile.html', data = {})


@app.route('/saveprofile', methods=['POST'])
@login_required
def saveprofile():
    if request.method == 'POST':
        return render_template('admin/editprofile.html', data = request.form)
