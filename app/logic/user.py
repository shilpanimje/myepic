from flask_login import login_user, current_user, logout_user

from app.models import user_details
from app.models import users
from app.models.user_details import UserDetails
from app.models.users import Users
from app import login_manager


@login_manager.user_loader
def load_user(email):
    return Users.query.filter_by(email=email).first()


def save_user(data):
    """save vendor  data.
    Args:
        data
    Returns:
        saved records.
    """
    return user_details.save_user(data)


def admin_login(data):
    """Admin login.
    Args:
        data
    Returns:
        data.
    """
    user_data = Users.query.filter_by(email=data['email'], password=data['password']).first()
    if user_data is None or user_data == '':
        return None

    users.update_authenticate(user_data)
    return login_user(user_data, remember=True)


def admin_register(data):
    """Admin register.
    Args:
        data
    Returns:
        data.
    """
    try:
        userexist = Users.query.filter_by(email=data['email']).first()
    except Exception as inst:
        userexist = None

    if userexist is None:
        result = users.register_user(data)
        user_details.add_user(result['email'], result['id'])
        return result
    return None


def logout():
    current_user.authenticated = False
    users.update_authenticate(current_user)
    return logout_user()


def get_user(id):
    return Users.query.filter_by(id=id).first()


def get_user_by_email(email):
    if not email:
        return None
    return Users.query.filter_by(email=email).first()


def get_user_details(user_id):

    if not id:
        return None

    result = UserDetails.query.filter_by(user_id=user_id).all()
    return result[0]


def update_user(data):
    """update user details  data.
    Args:
        data
    Returns:
        saved records.
    """

    user_details_data = UserDetails.query.filter_by(user_id=data['user_id']).all()
    if not user_details_data[0]:
        return None

    return user_details.update_user(data, user_details_data[0].id)





