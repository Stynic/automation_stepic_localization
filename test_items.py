import pytest
import time


def test_localization(browser, language):
    try:
        browser.get(
            f'http://selenium1py.pythonanywhere.com/{language}'
            f'/catalogue/coders-at-work_207/')
        button_submit = browser.find_element_by_css_selector(
            '.btn-add-to-basket').get_attribute('type')
        assert button_submit != None, f'Element not found!'
    finally:
        time.sleep(2)