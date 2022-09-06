
def my_print(func_name, *args):
    func_name = func_name.replace("_", " ").capitalize()
    print(func_name, end=" ")
    for arg in args:
        print(arg, end=" ")
    print()


def open_browser(browser_name):
    my_print(open_browser.__name__,  browser_name)


def go_to_company_name_homepage(page_url):
    my_print(go_to_company_name_homepage.__name__, page_url)


def find_registration_button_on_login_page(page_url, button_text):
    my_print(find_registration_button_on_login_page.__name__, page_url, button_text)


open_browser("Chrome")
go_to_company_name_homepage("https://qa.guru")
find_registration_button_on_login_page("https://qa.guru/python", "Начать обучение")
