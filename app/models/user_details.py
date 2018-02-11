import datetime
from sqlalchemy import Integer, Column, String, Date

from app import db


class UserDetails(db.Model):
    """user model."""

    __tablename__ = 'user_details'

    id = Column(Integer, nullable=False, autoincrement=True, primary_key=True)
    user_id = Column(Integer, nullable=False)
    name = Column(String)
    designation = Column(String)
    email = Column(String)
    altemail = Column(String)
    number = Column(Integer)
    gender = Column(String, default='M')
    status = Column(String, default='S')
    nationality = Column(String)
    bday = Column(Date)

    def __init__(self, user_id, name, designation, email, altemail, number, gender, status, nationality, bday):
        self.user_id = user_id
        self.name = name
        self.designation = designation
        self.email = email
        self.altemail = altemail
        self.number = number
        self.gender = gender
        self.status = status
        self.nationality = nationality
        self.bday = bday

    def to_dict(self):
        """return this data."""

        return {
            'id': self.id,
            'user_id': self.user_id,
            'name': self.name,
            'designation': self.designation,
            'email': self.email,
            'altemail': self.altemail,
            'number': self.number,
            'gender': self.gender,
            'status': self.status,
            'nationality': self.nationality,
            'bday': self.bday
        }


def save_user(data):
    """save vendor  data.
    Args:
        name(varchar), company(varchar)
    Returns:
        saved records.
    """

    new_user = UserDetails(
        user_id=data['user_id'].strip(),
        name=data['name'].strip(),
        designation=data['designation'].strip(),
        email=data['email'].strip(),
        altemail=data['altemail'].strip(),
        number=data['number'].strip(),
        gender=data['gender'].strip(),
        status=data['status'].strip(),
        nationality=data['nationality'].strip(),
        bday=datetime.datetime.utcnow()
    )
    db.create_all()
    db.session.add(new_user)
    db.session.commit()
    result = db.session.query(UserDetails).get(data['user_id'])
    return result.to_dict()


def add_user(email, user_id):
    new_user = UserDetails(
        user_id=user_id,
        name='',
        designation='',
        email=email,
        altemail='',
        number='',
        gender='M',
        status='S',
        nationality='Indian',
        bday=datetime.date.today()
    )
    db.create_all()
    db.session.add(new_user)
    db.session.commit()
    result = db.session.query(UserDetails).get(user_id)
    return result.to_dict()


def update_user(data, user_details_id=None):

    if user_details_id is None:
        return None

    new_user = dict([('user_id', data['user_id'].strip()),
        ('name', data['name'].strip()),
        ('designation', data['designation'].strip()),
        ('email', data['email'].strip()),
        ('altemail', data['altemail'].strip()),
        ('number', data['number'].strip()),
        ('gender', data['gender'].strip()),
        ('status', data['status'].strip()),
        ('nationality', data['nationality'].strip()),
        ('bday', datetime.datetime.strptime(data['bday'], "%Y-%m-%d"))])

    UserDetails.query.filter_by(id=user_details_id).update(new_user)
    db.session.commit()
    result = db.session.query(UserDetails).get(user_details_id)
    return result.to_dict()
