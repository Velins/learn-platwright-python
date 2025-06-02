from playwright.sync_api import Page, expect
from pages.login_page import LoginPage  

def test_TCP_1(page: Page):
    login_page = LoginPage(page)
    login_page.open()
    login_page.enter_username('standard_user')
    login_page.enter_password('secret_sauce')
    login_page.click_login_button()
    expect(page).to_have_url("https://www.saucedemo.com/v1/inventory.html")

def test_TCP_2(page: Page):
    login_page = LoginPage(page)
    login_page.open()
    login_page.enter_username('locked_out_user')
    login_page.enter_password('secret_sauce')
    login_page.click_login_button()
    expect(page).to_have_url("https://www.saucedemo.com/v1/index.html")
    expect(page.locator('[data-test="error"]')).to_have_text("Epic sadface: Sorry, this user has been locked out.")

def test_TCP_3(page: Page):
    login_page = LoginPage(page)
    login_page.open()
    login_page.enter_username('problem_user')
    login_page.enter_password('secret_sauce')
    login_page.click_login_button()
    expect(page).to_have_url("https://www.saucedemo.com/v1/inventory.html")

def test_TCP_4(page: Page):
    login_page = LoginPage(page)
    login_page.open()
    login_page.enter_username('performance_glitch_user')
    login_page.enter_password('secret_sauce')
    login_page.click_login_button()
    expect(page).to_have_url("https://www.saucedemo.com/v1/inventory.html")

def test_TCN_1(page: Page):
    login_page = LoginPage(page)
    login_page.open()
    login_page.enter_username('standard')
    login_page.enter_password('secret_sauce')
    login_page.click_login_button()
    expect(page).to_have_url("https://www.saucedemo.com/v1/index.html")
    expect(page.locator('[data-test="error"]')).to_have_text("Epic sadface: Username and password do not match any user in this service")

def test_TCN_2(page: Page):
    login_page = LoginPage(page)
    login_page.open()
    login_page.enter_username('locked_out')
    login_page.enter_password('secret_sauce')
    login_page.click_login_button()
    expect(page).to_have_url("https://www.saucedemo.com/v1/index.html")
    expect(page.locator('[data-test="error"]')).to_have_text("Epic sadface: Username and password do not match any user in this service")

def test_TCN_3(page: Page):
    login_page = LoginPage(page)
    login_page.open()
    login_page.enter_username('problem')
    login_page.enter_password('secret_sauce')
    login_page.click_login_button()
    expect(page).to_have_url("https://www.saucedemo.com/v1/index.html")
    expect(page.locator('[data-test="error"]')).to_have_text("Epic sadface: Username and password do not match any user in this service")

def test_TCN_4(page: Page):
    login_page = LoginPage(page)
    login_page.open()
    login_page.enter_username('performance_glitch')
    login_page.enter_password('secret_sauce')
    login_page.click_login_button()
    expect(page).to_have_url("https://www.saucedemo.com/v1/index.html")
    expect(page.locator('[data-test="error"]')).to_have_text("Epic sadface: Username and password do not match any user in this service")

def test_TCN_5(page: Page):
    login_page = LoginPage(page)
    login_page.open()
    login_page.enter_username('standard_user')
    login_page.enter_password('secret')
    login_page.click_login_button()
    expect(page).to_have_url("https://www.saucedemo.com/v1/index.html")
    expect(page.locator('[data-test="error"]')).to_have_text("Epic sadface: Username and password do not match any user in this service")

def test_TCN_6(page: Page):
    login_page = LoginPage(page)
    login_page.open()
    login_page.enter_username('locked_out_user')
    login_page.enter_password('secret')
    login_page.click_login_button()
    expect(page).to_have_url("https://www.saucedemo.com/v1/index.html")
    expect(page.locator('[data-test="error"]')).to_have_text("Epic sadface: Username and password do not match any user in this service")

def test_TCN_7(page: Page):
    login_page = LoginPage(page)
    login_page.open()
    login_page.enter_username('problem_user')
    login_page.enter_password('secret')
    login_page.click_login_button()
    expect(page).to_have_url("https://www.saucedemo.com/v1/index.html")
    expect(page.locator('[data-test="error"]')).to_have_text("Epic sadface: Username and password do not match any user in this service")

def test_TCN_8(page: Page):
    login_page = LoginPage(page)
    login_page.open()
    login_page.enter_username('performance_glitch_user')
    login_page.enter_password('secret')
    login_page.click_login_button()
    expect(page).to_have_url("https://www.saucedemo.com/v1/index.html")
    expect(page.locator('[data-test="error"]')).to_have_text("Epic sadface: Username and password do not match any user in this service")

def test_TCN_9(page: Page):
    login_page = LoginPage(page)
    login_page.open()
    login_page.enter_username('')
    login_page.enter_password('secret_sauce')
    login_page.click_login_button()
    expect(page).to_have_url("https://www.saucedemo.com/v1/index.html")
    expect(page.locator('[data-test="error"]')).to_have_text("Epic sadface: Username is required")

def test_TCN_10(page: Page):
    login_page = LoginPage(page)
    login_page.open()
    login_page.enter_username('standard_user')
    login_page.enter_password('')
    login_page.click_login_button()
    expect(page).to_have_url("https://www.saucedemo.com/v1/index.html")
    expect(page.locator('[data-test="error"]')).to_have_text("Epic sadface: Password is required")

def test_TCN_11(page: Page):
    login_page = LoginPage(page)
    login_page.open()
    login_page.enter_username('')
    login_page.enter_password('')
    login_page.click_login_button()
    expect(page).to_have_url("https://www.saucedemo.com/v1/index.html")
    expect(page.locator('[data-test="error"]')).to_have_text("Epic sadface: Username is required")