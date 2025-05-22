import pytest
from playwright.sync_api import Page

def test_login(page: Page) -> None:
    page.goto("http://18.117.154.106/auth/login")
    page.locator("xpath=//button[2]").click()
    page.locator("xpath=//html/body/app-root/app-signup/div/div/div/form/mat-form-field[1]/div[1]").click()
