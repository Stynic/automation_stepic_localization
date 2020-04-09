import pytest

from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',
                     help='Choose browser: chrome or firefox')
    parser.addoption('--language', action='store', default=None,
                     help='Choose language: en-gb or ru , etc.')


@pytest.fixture(scope='function')
def driver(request):
    browser_name = request.config.getoption('browser_name')

    browser = None
    if browser_name == 'chrome':
        print('\nstart chrome browser for test..')
        options = Options()
        options.add_experimental_option(
            'prefs', {'intl.accept_languages': 'user_language'})
        browser = webdriver.Chrome(options=options)
    elif browser_name == 'firefox':
        print('\nstart firefox browser for test..')
        fb = webdriver.FirefoxProfile()
        fb.set_preference("intl.accept_languages", user_language)
        browser = webdriver.Firefox(executable_path=GeckoDriverManager()
                                    .install(), firefox_profile=fb)
    else:
        raise pytest.UsageError('--browser_name should be chrome or firefox')
    yield browser
    print('\nquit browser..')
    browser.quit()


@pytest.fixture(scope='function')
def language(request):
    user_language = request.config.getoption('language')
    return user_language