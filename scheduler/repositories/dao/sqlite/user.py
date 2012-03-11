from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from repositories.dao.sqlite.base import Base

class User(Base):
    __tablename__ = 'users'

    user_id = Column(Integer, primary_key=True)
    name = Column(String)
    oauth_token = Column(String)
    oauth_secret = Column(String)