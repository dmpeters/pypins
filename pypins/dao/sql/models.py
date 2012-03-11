from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from pypins.dao.sql.base import Base

class Package(Base):
    __tablename__ = 'packages'

    package_id = Column(Integer, primary_key=True)
    name = Column(String)

class User(Base):
    __tablename__ = 'users'

    user_id = Column(Integer, primary_key=True)
    name = Column(String)
    oauth_token = Column(String)
    oauth_secret = Column(String)