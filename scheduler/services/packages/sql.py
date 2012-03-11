from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

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

    def add_package(self, package):
        self.session.add(package)
