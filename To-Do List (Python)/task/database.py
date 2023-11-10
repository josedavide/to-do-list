from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from base import Base


class Database:
    def __init__(self, db_url='sqlite:///todo.db?check_same_thread=False', echo=False):
        self.engine = create_engine(db_url, echo=echo)
        self.Session = sessionmaker(bind=self.engine)

    def dispose_engine(self):
        self.engine.dispose()
    def drop_and_create_db(self):
        Base.metadata.drop_all(bind=self.engine)
        Base.metadata.create_all(self.engine)
