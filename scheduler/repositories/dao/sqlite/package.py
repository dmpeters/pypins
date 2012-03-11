from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from repositories.dao.sqlite.base import Base

class Package(Base):
    __tablename__ = 'packages'

    package_id = Column(Integer, primary_key=True)
    name = Column(String)