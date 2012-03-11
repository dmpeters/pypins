from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Table
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from pypins.dao.sql.base import Base


# user_package = Table('user_package', Base.metadata,
#     Column('user_id', Integer, ForeignKey('users.user_id'), primary_key=True),
#     Column('package_id', Integer, ForeignKey('packages.package_id'), primary_key=True)
# )

class UserPackage(Base):
    __tablename__ = 'users_packages'
    subscription_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.user_id'))
    package_id = Column(Integer, ForeignKey('packages.package_id'))
    package = relationship("Package", backref="user_assocs")

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
    subscriptions = relationship("UserPackage", backref="users")
    # subscriptions = relationship("Package",
    #                 secondary=user_package,
    #                 backref="users")
