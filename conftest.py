from typing import Any, Generator
import pytest
from playwright.sync_api import sync_playwright, Page


@pytest.fixture(scope="session", autouse=True)
def page() -> Generator[Page, Any, None]:
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, timeout=400)
        context = browser.new_context()
        page = context.new_page()

        # login + navegação inicial
        page.goto("http://localhost:4200/auth/signup")
        page.locator("#username").fill("admin@adminteste.com")
        page.get_by_role("textbox", name="Senha").fill("admin_teste")
        page.get_by_role("button", name="Entrar").click()

        yield page

        context.close()
        browser.close()
