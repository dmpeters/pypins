from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class SqlUserService(object):

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

    def add_user(self, user):
        self.session.add(user)

    def register_package(self, user_id, package_id):
        pass

    def remove_package(self, user_id, package_id):
        pass
