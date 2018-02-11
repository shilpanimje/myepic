from app.models import user_education


def add_education(data):
    """save education  data.
    Args:
        data
    Returns:
        saved records.
    """
    return user_education.add_education(data)


# def get_skills(id=None):
#     """get list of skills data.
#     Returns:
#         get records.
#     """
#     if id is None:
#         return user_skills.get_skills()
#     else:
#         return user_skills.get_skills(id)
#
#
#
# def delete_project(id):
#     """delete projects data.
#     Returns:
#         delete project records.
#     """
#     project_data = user_projects.get_projects(id)
#     if not project_data:
#         return None
#
#     return user_projects.delete_project(id)
