import datetime

from flask_login import current_user
from sqlalchemy import Integer, Column, String, Date, Boolean, ForeignKey, Text
from sqlalchemy.orm import relationship

from app import db


class UserProjects(db.Model):
    """user projects model."""

    __tablename__ = 'user_projects'

    id = Column(Integer, nullable=False, autoincrement=True, primary_key=True)
    user_id = Column(Integer, nullable=False)
    name = Column(String)
    description = Column(Text)
    role = Column(String)
    technology = Column(String)
    team_size = Column(Integer)
    project_url = Column(String)

    def to_dict(self):
        """return this data."""

        return {
            'id': self.id,
            'user_id': self.user_id,
            'name': self.name,
            'description': self.description,
            'role': self.role,
            'technology': self.technology,
            'team_size': self.team_size,
            'project_url': self.project_url
        }


def add_project(data):
    """save project  data.
    Args:
        data
    Returns:
        saved records.
    """
    project = UserProjects(
        user_id=current_user.id,
        name=data['name'].strip(),
        description=data['description'].strip(),
        role=data['role'].strip(),
        technology=data['technology'].strip(),
        team_size=data['team_size'].strip(),
        project_url=data['project_url'].strip()
    )
    db.create_all()
    db.session.add(project)
    db.session.commit()
    return project.to_dict()


def get_projects(id=None):
    """get list of project data.
    args:
        id (optional)
    Returns:
        Porject list.
    """
    if id is not None:
        user_projects = UserProjects.query.filter_by(user_id=current_user.id, id=id).all()
    else:
        user_projects = UserProjects.query.filter_by(user_id=current_user.id).all()

    return user_projects


def delete_project(id):
    """delete project  data.
    Args:
        id
    Returns:
        delete project records.
    """
    obj = UserProjects.query.filter_by(id=id).one()
    db.session.delete(obj)
    db.session.commit()
    return True