import constants as const


class View:

    @staticmethod
    def show_main_menu_and_get_option():
        return View._show_menu_and_get_option(const.MAIN_MENU)

    @staticmethod
    def _show_menu_and_get_option(menu_content):
        menu_title, menu_options = menu_content
        View._show_menu(menu_title, menu_options)
        option = input()
        # if any(option == number for number, _ in menu_options.values()):
        return option

    @staticmethod
    def _show_menu(menu_title, options):
        print(menu_title)
        for (number, description) in options.values():
            print(number + ")", description)

    @staticmethod
    def _menu_option_code(menu, option):
        return menu[1][option][0]