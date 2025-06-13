import pytest


def test_login(page):
    page.goto("https://www.saucedemo.com/")
    page.fill("#user-name", "standard_user")
    page.fill("#password", "secret_sauce")
    page.click("#login-button")
    assert page.locator(".title").inner_text() == "Products"


def test_logout(page):
    # Perform login first
    page.goto("https://www.saucedemo.com/")
    page.fill("#user-name", "standard_user")
    page.fill("#password", "secret_sauce")
    page.click("#login-button")
    assert page.locator(".title").inner_text() == "Products"

    # Now logout
    page.wait_for_selector("#react-burger-menu-btn")
    page.click("#react-burger-menu-btn")
    page.wait_for_selector("//nav/a[text()='Logout']")
    page.click("//nav/a[text()='Logout']")
    page.wait_for_selector("#login-button")
