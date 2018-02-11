import datetime

from flask_login import current_user
from sqlalchemy import Integer, Column, String, Date, Boolean, ForeignKey, Text
from sqlalchemy.orm import relationship

from app import db


class UserSkills(db.Model):
    """user skills model."""

    __tablename__ = 'user_skills'

    id = Column(Integer, nullable=False, autoincrement=True, primary_key=True)
    user_id = Column(Integer, nullable=False)
    technical_skills = Column(Text)
    database_skills = Column(Text)
    frameworks = Column(Text)
    language_speaks = Column(String)
    achievements = Column(Text)
    extra_curricular_data = Column(Text)
    summary = Column(Text)

    def to_dict(self):
        """return this data."""

        return {
            'id': self.id,
            'user_id': self.user_id,
            'technical_skills': self.technical_skills,
            'database_skills': self.database_skills,
            'frameworks': self.frameworks,
            'language_speaks': self.language_speaks,
            'achievements': self.achievements,
            'extra_curricular_data': self.extra_curricular_data,
            'summary': self.summary
        }


def add_skills(data):
    """save skills  data.
    Args:
        data
    Returns:
        saved records.
    """
    skills = UserSkills(
        user_id=current_user.id,
        technical_skills=data['technical_skills'].strip(),
        database_skills=data['database_skills'].strip(),
        frameworks=data['frameworks'].strip(),
        language_speaks=data['language_speaks'].strip(),
        achievements=data['achievements'].strip(),
        extra_curricular_data=data['extra_curricular_data'].strip(),
        summary=data['summary'].strip()
    )

    try:
        user_skills_data = UserSkills.query.filter_by(user_id=current_user.id).one()
        db.session.query(UserSkills).filter(UserSkills.id == user_skills_data.id). \
            update({
                'technical_skills': data['technical_skills'].strip(),
                'database_skills': data['database_skills'].strip(),
                'frameworks': data['frameworks'].strip(),
                'language_speaks': data['language_speaks'].strip(),
                'achievements': data['achievements'].strip(),
                'extra_curricular_data': data['extra_curricular_data'].strip(),
                'summary': data['summary'].strip()})
    except Exception as inst:
        db.create_all()
        db.session.add(skills)

    db.session.commit()
    return skills.to_dict()


def get_skills(id=None):
    """get skills  data.
    Args:
        data
    Returns:
        get records.
    """

    if id is None:
        try:
            user_skills_data = UserSkills.query.filter_by(user_id=current_user.id).one()
        except Exception as inst:
            return True
    else:
        user_skills_data = UserSkills.query.filter_by(user_id=current_user.id, id=id).one()
    return user_skills_data.to_dict()
