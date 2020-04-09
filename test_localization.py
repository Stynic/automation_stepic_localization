import pytest
import time


def test_localization(driver, language):
    try:
        driver.get(
            f'http://selenium1py.pythonanywhere.com/{language}/catalogue/coders-at-work_207/')
        button_submit = driver.find_element_by_css_selector('.btn-add-to-basket').get_attribute('type')
        assert button_submit == 'submit', f'На странице нет кнопки submit'
    finally:
        time.sleep(5)