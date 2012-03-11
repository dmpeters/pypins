from sqlalchemy.sql.expression import text
from sqlalchemy.sql.expression import delete
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import InvalidRequestError
from pypins.dao.sql.models import UserPackage

class SqlUserService(object):

    def __init__(self):
        # TODO engine and session initialization should be moved out
        # to a factory. echo will log out all commands
        self.engine = create_engine('sqlite:///../pypins.db', echo=True)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    def __enter__(self):
        try:
            self.session.begin()
            print("begin transaction")
        except InvalidRequestError:
            pass
        
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.commit()
        return True

    def add_user(self, user):
        self.session.add(user)

    def register_subscription(self, user_id, package_id):
        subscription = UserPackage()
        subscription.user_id = user_id
        subscription.package_id = package_id
        self.session.add(subscription)

    def remove_subscription(self, user_id, package_id):
        table = UserPackage.__table__
        self.session.execute(delete(table).where(table.c.user_id==user_id).where(table.c.package_id==package_id))
