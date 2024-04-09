from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_guest_should_see_cart_button_pass(browser):
    browser.get(link)
    add_cart = browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket")
    try:
        WebDriverWait(browser, 10).until(EC.element_to_be_clickable(add_cart))
        cart_btn = True
    except:
        cart_btn = False
    assert cart_btn
