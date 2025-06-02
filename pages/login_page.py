from playwright.sync_api import expect

USERNAME_FIELD = '#user-name'
PASSWORD_FIELD = '#password'

class LoginPage:

    def __init__(self, page):
        self.page = page

    def open(self):
        self.page.goto("https://www.saucedemo.com/v1/index.html")

    def enter_username(self, username):
        self.page.locator(USERNAME_FIELD).fill(username)

    def enter_password(self, password):
        self.page.locator(PASSWORD_FIELD).fill(password)

    def click_login_button(self):
        self.page.locator('#login-button').click()