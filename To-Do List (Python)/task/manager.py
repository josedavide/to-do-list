from datetime import datetime, timedelta


class Manager:
    def __init__(self, repository):
        self.repo = repository

    def reset_database(self):
        self.repo.reset_database()

    def dispose_database(self):
        self.repo.dispose_database()

    def get_all_tasks(self):
        return list(self.repo.list_all_tasks())

    def get_missed_tasks(self):
        return list(self.repo.list_missed_tasks())

    def get_today_tasks(self):
        return list(self.repo.list_date_tasks(datetime.today().date()))

    def get_week_tasks(self):
        week_tasks = {}
        for i in range(7):
            date = datetime.today().date() + timedelta(days=i)
            week_tasks[date.strftime('%A %d %b:')] = list(self.repo.list_date_tasks(date))
        return week_tasks

    def add_task(self, task_name, deadline=datetime.today()):
        self.repo.add_task(task_name, deadline)

    def delete_task_by_id(self, id_task):
        self.repo.delete_task_by_id(id_task)

