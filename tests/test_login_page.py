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
    expect(page.get_by_role("error", name="Epic sadface: Sorry, this user has been locked out.")).to_be_visible

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