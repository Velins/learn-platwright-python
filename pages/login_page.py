from playwright.sync_api import expect

USERNAME_FIELD = '#user-name'
PASSWORD_FIELD = '#password'
BUTTON_LOGIN_NAME = 'Login'
LOCKED_OUT_MESSAGE = 'Epic sadface: Sorry, this user has been locked out.'

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
        self.page.get_by_role('button', name=BUTTON_LOGIN_NAME).click()
    
    def check_relocation_to_home_page(self):
        expect(self.page).to_have_url("https://www.saucedemo.com/v1/inventory.html")
    
    def check_login_location(self):
        expect(self.page).to_have_url("https://www.saucedemo.com/v1/index.html")
    
    def check_validation_locked_out_message(self):
        expect(self.page.get_by_role("error", name=LOCKED_OUT_MESSAGE)).to_be_visible