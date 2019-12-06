import pytest
from selenium import webdriver
import time

def test_button_add_to_basket(browser):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
#    time.sleep(30)
    button = len(browser.find_elements_by_css_selector("button.btn.btn-lg.btn-primary.btn-add-to-basket"))
    assert button > 0, "No button add-to-basket on the page"
