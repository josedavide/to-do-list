from datetime import datetime, date
from model import Task

class Repository:
    def __init__(self, database):
        self.db = database

    def reset_database(self):
        self.db.drop_and_create_db()

    def dispose_database(self):
        self.db.dispose_engine()

    def list_all_tasks(self):
        # with self.db.Session() as session:
        session = self.db.Session()
        try:
            query_result = session.query(Task).order_by(Task.deadline).all()
            return query_result
        finally:
            session.close()

    def list_missed_tasks(self, day):
        # with self.db.Session() as session:
        session = self.db.Session()
        try:
            query_result = session.query(Task).filter(Task.deadline < day).order_by(Task.deadline).all()
            return query_result
        finally:
            session.close()

    def list_date_tasks(self, day):
        #with self.db.Session() as session:
        session = self.db.Session()
        try:
            query = session.query(Task)
            query_result = query.filter(Task.deadline == day).all()
            return query_result
        finally:
            session.close()


    def add_task(self, task, deadline):
        # with self.db.Session() as session:
        session = self.db.Session()
        try:
            registry = Task(task=task, deadline=deadline)
            session.add(registry)
            session.commit()
        finally:
            session.close()

    def delete_task_by_id(self, id_task):
        session = self.db.Session()
        try:
            task = session.query(Task).filter(Task.id == id_task).first()
            if task:
                session.delete(task)
                session.commit()
        finally:
            session.close()
