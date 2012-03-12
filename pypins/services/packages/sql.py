from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import joinedload
from sqlalchemy.orm import join
from sqlalchemy.sql.expression import delete
from pypins.dao.sql.models import UserPackage
from pypins.dao.sql.models import Package
from pypins.dao.sql.models import User

class SqlPackageService(object):

    def __init__(self):
        # TODO engine and session initialization should be moved out
        # to a factory. echo will log out all commands
        engine = create_engine('sqlite:///../pypins.db', echo=False)
        Session = sessionmaker(bind=engine)
        self.session = Session()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.commit()
        return True

    def get_subscriptions_for_user(self, user_id):
        return self.session.query(UserPackage).\
        options(joinedload(UserPackage.users)).\
        filter_by(user_id=user_id).all()

    def get_subscriptions_for_package(self, package_name):
        return self.session.query(UserPackage).\
        options(joinedload(UserPackage.users)).\
        filter_by(package_name=package_name).all()


    def add_package(self, package):
        self.session.add(package)

    def rmeove_package(self, package):
        self.session.delete(package)

    def register_subscription(self, user_id, package_name):
        subscription = UserPackage()
        subscription.user_id = user_id
        subscription.package_name = package_name
        self.session.add(subscription)

    def remove_subscription(self, user_id, package_name):
        table = UserPackage.__table__
        self.session.execute(delete(table).where(table.c.user_id==user_id).where(table.c.package_name==package_name))
