from flask_login import current_user

from app import app
from app.models import user_projects


def add_project(data):
    """save vendor  data.
    Args:
        data
    Returns:
        saved records.
    """
    return user_projects.add_project(data)


def get_projects(id=None):
    """get list of projects data.
    Returns:
        saved records.
    """
    if id is None:
        return user_projects.get_projects()
    else:
        return user_projects.get_projects(id)


def delete_project(id):
    """delete projects data.
    Returns:
        delete project records.
    """
    project_data = user_projects.get_projects(id)
    if not project_data:
        return None

    return user_projects.delete_project(id)


def upload_project_image(file_data, project_data):
    """delete projects data.
    Returns:
        delete project records.
    """
