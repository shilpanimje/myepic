from flask_login import login_user

from app.models import user_details
from app.models import users
from app.models.users import Users
from app import login_manager


@login_manager.user_loader
def load_user(email):
    return Users.query.get(email)


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
    user = Users.query.filter_by(email=data['email'], password=data['password']).first()
    if user is None or user == '':
        return False

    return login_user(user)


    #return users.admin_login(data)


