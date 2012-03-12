from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import InvalidRequestError

class SqlUserService(object):

    def __init__(self):
        # TODO engine and session initialization should be moved out
        # to a factory. echo will log out all commands
        self.engine = create_engine('sqlite:///../pypins.db', echo=False)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    def __enter__(self):
        try:
            self.session.begin()
        except InvalidRequestError:
            pass
        
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.commit()
        return True

    def add_user(self, user):
        self.session.add(user)
