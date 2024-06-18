import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en',  # Default language set to 'en'
                     help="Choose UI language: en or fr")

@pytest.fixture(scope="function")
def browser(request):
    browser_lang = request.config.getoption("language")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': browser_lang})
    print(f"\nStart browser for test in {browser_lang} localisation..")
    
    browser = webdriver.Chrome(options=options)

    yield browser
    print("\nquit browser..")
    browser.quit()