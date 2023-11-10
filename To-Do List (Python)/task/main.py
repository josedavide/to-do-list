from database import Database
from manager import Manager
from repository import Repository
from ui_controller import UiController

class Main:
    def __init__(self):

        repository = Repository(Database())
        self.manager = Manager(repository)

        self.ui_controller = UiController(self.manager)

    def drop_and_create_database(self):
        try:
            self.manager.reset_database()
        except Exception as e:
            print("DB Initialization error:", e)
        #else:
        #    print("Database created successfully!")

    def launch_ui(self):
        self.ui_controller.manage_main_menu()


if __name__ == '__main__':
    main = Main()
    try:
        main.drop_and_create_database()
        main.launch_ui()
    except Exception as e:
        print(f"================ CIERRE ================ \n==>> Ocurrió un error no manejado: <<== \n{e}")
    finally:
        main.manager.dispose_database()
