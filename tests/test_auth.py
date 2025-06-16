import pytest
from playwright.sync_api import Page

@pytest.mark.usefixtures("page")
def test_register(page: Page) -> None:
    page = page
    page.locator("xpath=/app-signup/div/div/div/form/mat-form-field[1]/div[1]/div/div[2]/input").click()
    page.get_by_role("textbox", name="Digite seu nome").click()
    page.get_by_role("textbox", name="Digite seu nome").fill("user teste")
    page.get_by_role("textbox", name="Digite seu e-mail").click()
    page.get_by_role("textbox", name="Digite seu e-mail").fill("teste@teste.com")
    page.get_by_role("textbox", name="Digite seu apelido").click()
    page.get_by_role("textbox", name="Digite seu apelido").fill("user teste")
    page.get_by_role("textbox", name="Digite sua senha").click()
    page.get_by_role("textbox", name="Digite sua senha").fill("12345678")
    page.get_by_role("textbox", name="Confirmar senha").click()
    page.get_by_role("textbox", name="Confirmar senha").fill("12345678")
    page.get_by_role("button", name="Salvar").click()
    page.get_by_text("schoolBit ClassAulas e").click()
    page.get_by_role("button", name="Novo").click()
    page.get_by_role("textbox", name="Nome da Sala").click()
    page.get_by_role("textbox", name="Nome da Sala").fill("sala teste")
    page.get_by_role("textbox", name="Descrição").click()
    page.get_by_role("textbox", name="Descrição").fill("descrição teste")
    page.get_by_text("Selecione os dias").click()
    page.get_by_role("option", name="Segunda").click()
    page.get_by_role("option", name="Terça").click()
    page.get_by_role("option", name="Quinta").click()
    page.locator(".cdk-overlay-container > div:nth-child(3)").click()
    page.locator("div").filter(has_text="Turma carregada com sucesso!").nth(2).click()
    page.get_by_text("home Início").click()
    page.get_by_role("heading", name="sala teste").click()
    page.get_by_text("Digite seu e-mail").fill("teste@teste.com")
    page.get_by_text("Digite sua senha").fill("12345678")
    page.get_by_text("Entrar").click()
    boolean = bool(page.locator("xpath=app-select-plataform").get_by_text("Escolha uma plataforma para acessar"))
    assert boolean == True


@pytest.mark.usefixtures("page")
def test_login(page: Page) -> None:
    page = page
    page.get_by_role("textbox", name="Digite seu e-mail").click()
    page.get_by_role("textbox", name="Digite seu e-mail").fill("teste@teste.com")
    page.get_by_role("textbox", name="Digite sua senha").click()
    page.get_by_role("textbox", name="Digite sua senha").fill("12345678")
    page.get_by_role("button", name="Entrar").click()
    assert True


@pytest.mark.usefixtures("page")
def test_login_auth(page: Page) -> None:
    page = page
    page.wait_for_url("http://localhost:4200/select-plataform")

    # Verifica se token está no localStorage
    token = page.evaluate("() => localStorage.getItem('access')")
    assert token is not None, "Token JWT/ não foi encontrado no localStorage"
    assert len(token) > 20, "Token JWT parece inválido"
