from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_localisation_check(browser):
    browser.get(link)
    
    # Wait for the purchase button to be present
    purchase_buttons = WebDriverWait(browser, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".add-to-basket > .btn"))
    )
    
    # Assert that the list is not empty
    assert len(purchase_buttons) > 0, "Button is missing on the page"
    time.sleep(5)