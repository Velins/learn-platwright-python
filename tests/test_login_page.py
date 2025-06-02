from playwright.sync_api import Page
from pages.login_page import LoginPage  

def test_TCP_1(page: Page):
    login_page = LoginPage(page)
    login_page.open()
    login_page.enter_username('standard_user')
    login_page.enter_password('secret_sauce')
    login_page.click_login_button()
    login_page.check_relocation_to_home_page()

def test_TCP_2(page: Page):
    login_page = LoginPage(page)
    login_page.open()
    login_page.enter_username('locked_out_user')
    login_page.enter_password('secret_sauce')
    login_page.click_login_button()
    login_page.check_login_location()
    login_page.check_validation_locked_out_message()

def test_TCP_3(page: Page):
    login_page = LoginPage(page)
    login_page.open()
    login_page.enter_username('problem_user')
    login_page.enter_password('secret_sauce')
    login_page.click_login_button()
    login_page.check_relocation_to_home_page()

def test_TCP_4(page: Page):
    login_page = LoginPage(page)
    login_page.open()
    login_page.enter_username('performance_glitch_user')
    login_page.enter_password('secret_sauce')
    login_page.click_login_button()
    login_page.check_relocation_to_home_page()