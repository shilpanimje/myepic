import datetime

from flask_login import current_user
from sqlalchemy import Integer, Column, String, Date, Boolean, ForeignKey, Text, ForeignKey
from sqlalchemy.orm import relationship, backref

from app import db

class EducationTypes(db.Model):
    """user skills model."""

    __tablename__ = 'education_types'

    id = Column(Integer, nullable=False, autoincrement=True, primary_key=True)
    education_name = Column(String)
    EducationDetails = relationship('EducationDetails', backref='EducationTypes')

    def to_dict(self):
        """return this data."""

        return {
            'id': self.id,
            'education_name': self.education_name
        }


class EducationDetails(db.Model):
    """user skills model."""

    __tablename__ = 'education_details'

    id = Column(Integer, nullable=False, autoincrement=True, primary_key=True)
    user_id = Column(Integer, nullable=False)
    education_type_id = Column(Integer, ForeignKey('education_types.id'))
    university = Column(String)
    percentage = Column(String)

    def to_dict(self):
        """return this data."""

        return {
            'id': self.id,
            'user_id':self.user_id,
            'education_type_id': self.education_type_id,
            'university': self.university,
            'percentage': self.percentage
        }


def add_education(data):
    """save education  data.
    Args:
        data
    Returns:
        saved records.
    """
    education_types = EducationTypes.query.filter_by().all()

    education_data_10 = EducationDetails(
        user_id=current_user.id,
        education_type_id=education_types[0].id,
        university=data.get('tenth_university',''),
        percentage=data.get('tenth_percentage','')
    )
    education_data_12 = EducationDetails(
        user_id=current_user.id,
        education_type_id=education_types[1].id,
        university=data.get('twelth_university',''),
        percentage=data.get('twelth_percentage','')
    )
    education_data_graduate = EducationDetails(
        user_id=current_user.id,
        education_type_id=education_types[2].id,
        university=data.get('graduate_university',''),
        percentage=data.get('graduate_percentage','')
    )
    db.create_all()
    db.session.add_all([education_data_10,education_data_12,education_data_graduate])
    db.session.commit()
    return True
#
#
# def get_skills(id=None):
#     """get skills  data.
#     Args:
#         data
#     Returns:
#         get records.
#     """
#     if id is None:
#         user_skills = UserSkills.query.filter_by(user_id=current_user.id).one()
#     else:
#         user_skills = UserSkills.query.filter_by(user_id=current_user.id, id=id).one()
#     return user_skills.to_dict()
