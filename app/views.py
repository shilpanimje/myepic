import os
from flask import render_template, request, flash, url_for
from flask_login import login_required, current_user
from werkzeug.utils import redirect

from app import app
from app.logic import user, contact
from app.logic import project, skill, education
from app.forms import AddProjectForm, LoginForm, RegisterForm, EditProfileForm, AddSkillsForm, AddEducationForm, \
    EmailPopForm
from werkzeug.utils import secure_filename


@app.route('/')
def index():
    email_form = EmailPopForm(request.form)
    # user_details = user.get_user_details()
    return render_template('frontend/uicookie/email-pop.html', form=email_form)


@app.route('/myportfolio', methods=['GET', 'POST'])
def myportfolio():
    if request.form['email']:
        user_login_data = user.get_user_by_email(request.form['email'])
        user_details_data = user.get_user_details(user_login_data.id)
        user_skills_data = skill.get_skills(user_login_data.id)
        return render_template('frontend/uicookie/index.html', user=user_details_data, skills=user_skills_data)
    email_form = EmailPopForm(request.form)
    return render_template('frontend/uicookie/email-pop.html', form=email_form)


@app.route('/about')
def about():
    return render_template('frontend/about.html')


@app.route('/adminlogin', methods=['GET', 'POST'])
def admin_login():
    login_form = LoginForm(request.form)

    if request.method == 'POST' and login_form.validate():
        result = user.admin_login(request.form)
        if result is None:
            flash('Username or Password is invalid', 'error')
            return redirect(url_for('admin_login'))
        flash('Logged in successfully')
        return redirect(url_for('dashboard'))
    return render_template('admin/login.html', form=login_form)


@app.route('/adminregister', methods=['GET', 'POST'])
def admin_register():
    register_form = RegisterForm(request.form)
    if request.method == 'POST' and register_form.validate():
        result = user.admin_register(request.form)
        if result is None:
            flash('Email exist. Please use another one', 'error')
            return redirect(url_for('admin_register'))
        flash('Registered successfully. Please login')
        return redirect(url_for('admin_login'))
    return render_template('admin/register.html', form=register_form)


@app.route('/logout', methods=['GET'])
@login_required
def logout():
    user.logout()
    flash('User logout successfully.')
    return redirect(url_for('admin_login'))


@app.route('/adminforgotpass')
def admin_forgot_password():
    return render_template('admin/forgot_password.html')


@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('admin/dashboard.html')


@app.route('/editprofile', methods=['POST', 'GET'])
@login_required
def edit_profile():
    if not current_user.id:
        return render_template('admin/error.html')

    userdata = user.get_user_details(current_user.id)
    editprofile_form = EditProfileForm(request.form, obj=userdata)

    if request.method == 'POST' and editprofile_form.validate():
        userdata = user.update_user(request.form)
        return render_template('admin/editprofile.html', form=editprofile_form)
    else:
        editprofile_form.populate_obj(userdata)
        return render_template('admin/editprofile.html', form=editprofile_form, id=userdata.id)


@app.route('/saveprofile', methods=['POST'])
@login_required
def saveprofile():
    if request.method == 'POST':
        return render_template('admin/editprofile.html', data=request.form)


@app.route('/userprojects', methods=['GET'])
@login_required
def user_projects():
    return render_template('admin/projects.html', projects=project.get_projects())


@app.route('/addproject', methods=['GET', 'POST'])
@login_required
def add_project():
    addproject_form = AddProjectForm(request.form)
    if request.method == 'POST':
        project.add_project(request.form)
        flash('Project added successfully')
        return redirect(url_for('user_projects'))
    return render_template('admin/addproject.html', form=addproject_form)


@app.route('/deleteproject/<path:id>', methods=['GET'])
@login_required
def delete_project(id):
    if not id:
        flash('Required project id.')
        return redirect(url_for('user_projects'))
    result = project.delete_project(id)
    if result is None:
        flash('Project not exist.')
        return redirect(url_for('user_projects'))
    else:
        flash('Project deleted successfully.')
        return redirect(url_for('user_projects'))


@app.route('/updateproject/<path:id>', methods=['GET', 'POST'])
@login_required
def update_project(id):
    if not id:
        flash('Required project id.')
        return redirect(url_for('user_projects'))

    result = project.get_projects(id)
    addproject_form = AddProjectForm(obj=result[0])
    addproject_form.populate_obj(result[0])

    return render_template('admin/addproject.html', form=addproject_form)


@app.route('/addskills', methods=['GET', 'POST'])
@login_required
def add_skills():
    addskill_form = AddSkillsForm(request.form)
    if request.method == 'POST':
        result = skill.add_skills(request.form)
        if result:
            flash('Skills added successfully.')
            return redirect(url_for('add_skills'))
    return render_template('admin/addskills.html', form=addskill_form, data=skill.get_skills())


@app.route('/educationdetails', methods=['GET', 'POST'])
@login_required
def add_education_details():
    addeducation_form = AddEducationForm(request.form)
    if request.method == 'POST':
        result = education.add_education(request.form)
        if result:
            flash('Added successfully.')
            return redirect(url_for('add_education_details'))
    return render_template('admin/educationdetails.html', form=addeducation_form)


@app.route('/upload_image/<path:id>')
@login_required
def upload_project_image(id):
    return render_template('admin/upload_image.html', project_id=id)


@app.route('/upload', methods=['POST'])
@login_required
def upload():
    if not request.form['project_id']:
        return render_template('admin/project.html', projects=project.get_projects())
    project_data = project.get_projects(request.form['project_id'])

    if request.method == 'POST':
        # check if the post request has the file part
        if 'project_photo' not in request.files:
            flash('No file part')
            return render_template('admin/upload_image.html', project_id=request.form['project_id'])
        file = request.files['project_photo']
        if file.filename == '':
            flash('No selected file')
            return render_template('admin/upload_image.html', project_id=request.form['project_id'])

        if file and allowed_file(file.filename):
            filename = file.filename
            extension = filename.rsplit('.', 1)[1].lower()
            filename = secure_filename(project_data[0].name + '_image.' + extension)
            destination_folder = app.config['UPLOAD_FOLDER'] + '/' + request.form['project_id']

            if not os.path.exists(destination_folder):
                print(destination_folder)
                exit()
                os.makedirs(destination_folder)

            file.save(os.path.join(destination_folder, filename))
            return render_template('admin/upload_image.html', project_id=request.form['project_id'])


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config["ALLOWED_EXTENSIONS"]


@app.route('/contactus', methods=['POST'])
def contact_us():
    print(request.method)
    if request.method == 'POST':
        result = contact.send_mail(request.form)
    return result

