from wtforms import Form, StringField, PasswordField, validators, IntegerField, TextAreaField, RadioField, DateField


class LoginForm(Form):
    email = StringField('email', [
        validators.DataRequired()])
    password = PasswordField('New Password', [
        validators.DataRequired(),
        validators.Length(min=8, max=20)
    ])


class RegisterForm(Form):
    email = StringField('email', [
        validators.DataRequired(), validators.Email()])
    password = PasswordField('Password', [
        validators.DataRequired(), validators.Length(min=8, max=20)])
    confirm_password\
        = PasswordField('Confirm Password', [
        validators.DataRequired(), validators.EqualTo('password', 'Confirm password should match with password')])
    confirm_password \
        = PasswordField('Confirm Password', [
        validators.DataRequired(), validators.EqualTo('password', 'Confirm password should match with password')])


class EditProfileForm(Form):
    name = StringField('Name', [validators.DataRequired(), validators.length(max=50)])
    designation = StringField('Enter Your Designation', [validators.DataRequired()])
    email = StringField('Email', [validators.DataRequired(), validators.Email()])
    altemail = StringField('Alternate Email', [validators.Email()])
    number = IntegerField('Mobile Number', [validators.required()])
    gender = RadioField('Gender', choices=[('M','Male'),('F','Female')], default='M')
    status = RadioField('Status', choices=[('S','Single'),('M','Married')], default='S')
    nationality = StringField('Natinality', [validators.DataRequired()])
    bday = DateField('Birth date', [validators.DataRequired()])


class AddProjectForm(Form):
    name = StringField('Name')
    description = StringField('Description')
    role = StringField('Role')
    technology = StringField('Technology')
    team_size = IntegerField('Team Size')
    project_url = StringField('Project Url')


class AddSkillsForm(Form):
    technical_skills = StringField('Technical Skills', render_kw={'placeholder':'Add comma seperated skills'})
    database_skills = StringField('Database Skills', render_kw={'placeholder': 'Add comma seperated skill'})
    frameworks = StringField('Frameworks / CMS', render_kw={'placeholder': 'Add comma seperated names'})
    language_speaks = StringField('Language Speaks', render_kw={'placeholder':'Add comma seperated languages'})
    achievements = TextAreaField('Your Acievements', render_kw={'placeholder':'Add comma seperated achievments'})
    extra_curricular_data = TextAreaField('Extra Curricular Activities', render_kw={'placeholder':'Add comma seperated activities'})
    summary = TextAreaField('Resume Summary', render_kw={'placeholder':'Add resume summary'})


class AddEducationForm(Form):
    tenth_university = StringField('10th University', render_kw={'placeholder':'Add 10th University Name'})
    twelth_university = StringField('12th University', render_kw={'placeholder': 'Add 12th University Name'})
    gruduate_university = StringField('Graduation University', render_kw={'placeholder': 'Add Graduation University Name'})
    post_graduate_university = StringField('Post Graduation University', render_kw={'placeholder': 'Add Post Graduation University Name'})
    tenth_percentage = StringField('10th Percentage', render_kw={'placeholder': 'Add 10th Percentage'})
    twelth_percentage = StringField('12th Percentage', render_kw={'placeholder': 'Add 12th Percentage'})
    graduate_percentage = StringField('Graduation Percentage', render_kw={'placeholder': 'Add Graduate Percentage'})
    post_graduate_percentage = StringField('Post Graduation  Percentage', render_kw={'placeholder': 'Add Post Graduation Percentage'})


class EmailPopForm(Form):
    email = StringField('email', [
        validators.DataRequired()])
