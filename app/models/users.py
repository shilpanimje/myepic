import datetime
from sqlalchemy import Integer, Column, String, Date, Boolean

from app import db


class Users(db.Model):
    """user model."""

    __tablename__ = 'users'

    id = Column(Integer, nullable=False, autoincrement=True, primary_key=True)
    email = Column(String)
    password = Column(String)
    authenticated = Column(Boolean, default=False)
    date_created = Column(Date)

    def __init__(self, email, password, date_created):
        self.email = email
        self.password = password
        self.date_created = date_created

    def is_active(self):
        """True, as all users are active."""
        return True

    def get_id(self):
        """Return the email address to satisfy Flask-Login's requirements."""
        return self.email

    def is_authenticated(self):
        """Return True if the user is authenticated."""
        return self.authenticated

    def is_anonymous(self):
        """False, as anonymous users aren't supported."""
        return False

    def to_dict(self):
        """return this data."""

        return {
            'id': self.id,
            'email': self.email,
            'password': self.password,
            'authenticated': self.authenticated,
            'date_created': self.date_created
        }


def update_authenticate(user_data):
    """Update authenticate true/false for login.
    Args:
        user_data
    Returns:
        True.
    """
    db.session.add(user_data)
    db.session.commit()


def register_user(data):
    """save vendor  data.
    Args:
        data
    Returns:
        saved records.
    """
    new_user = Users(
        email=data['email'].strip(),
        password=data['password'].strip(),
        date_created=datetime.datetime.utcnow()
    )
    db.create_all()
    db.session.add(new_user)
    db.session.commit()
    return new_user.to_dict()
