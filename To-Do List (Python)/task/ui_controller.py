from datetime import datetime
import constants as const
from manager import Manager
from view import View

class UiController:

    def __init__(self, manager):
        self.manager = manager
        self.view = View()

    def manage_main_menu(self):
        while True:
            option = self.view.show_main_menu_and_get_option()

            if option == UiController._menu_option_code(const.MAIN_MENU, const.MAIN_EXIT):
                print('Bye!')
                return
            elif option == UiController._menu_option_code(const.MAIN_MENU, const.MAIN_TODAY_TASKS):
                self.show_today_tasks()
            elif option == UiController._menu_option_code(const.MAIN_MENU, const.MAIN_WEEK_TASKS):
                self.show_week_tasks()
            elif option == UiController._menu_option_code(const.MAIN_MENU, const.MAIN_ALL_TASKS):
                self.show_all_tasks()
            elif option == UiController._menu_option_code(const.MAIN_MENU, const.MAIN_MISSED_TASKS):
                self.show_missed_tasks()
            elif option == UiController._menu_option_code(const.MAIN_MENU, const.MAIN_ADD_TASK):
                self.add_task()
            elif option == UiController._menu_option_code(const.MAIN_MENU, const.MAIN_DELETE_TASK):
                self.delete_task()

    def show_today_tasks(self):
        tasks = self.manager.get_today_tasks()
        print(f"Today {datetime.today().date().strftime('%d %b:')}")
        if not tasks:
            print("Nothing to do!")
        else:
            print('\n'.join([f"{task.id}. {task.task}" for task in tasks]))

    def show_week_tasks(self):
        week_tasks = self.manager.get_week_tasks()
        for day, tasks in week_tasks.items():
            print()
            print(day)
            if not tasks:
                print("Nothing to do!")
            else:
                print('\n'.join([f"{task.id}. {task.task}" for task in tasks]))

    def show_all_tasks(self):
        tasks = self.manager.get_all_tasks()
        print("All tasks:")
        if not tasks:
            print("Nothing to do!")
        else:
            print('\n'.join([f"{task.id}. {task.task}. {task.deadline.strftime('%d %b')}" for task in tasks]))

    def show_missed_tasks(self):
        tasks = self.manager.get_all_tasks()
        print("Missed tasks:")
        if not tasks:
            print("Nothing to do!")
        else:
            print('\n'.join([f"{task.id}. {task.task}. {task.deadline.strftime('%d %b')}" for task in tasks]))

    def add_task(self):
        name = input("Enter a task\n")
        date_text = input("Enter a deadline\n")
        date_format = "%Y-%m-%d"
        self.manager.add_task(name, datetime.strptime(date_text, date_format))
        print("The task has been added!")

    def delete_task(self):
        id_task = self._list_and_select_task()
        if id_task is not None:
            self.manager.delete_task_by_id(id_task)
            print("The task has been deleted!")

    def _list_and_select_task(self):
        print("Choose the number of the task you want to delete:\n")
        tasks = self.manager.get_all_tasks()
        if not tasks:
            print("Nothing to delete")
            return None
        else:
            print('\n'.join([f"{task.id}. {task.task}. {task.deadline.strftime('%d %b')}" for task in tasks]))
        id_task = int(input())
        return id_task

    @staticmethod
    def _menu_option_code(menu, option):
        return menu[1][option][0]