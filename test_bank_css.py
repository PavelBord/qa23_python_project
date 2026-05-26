import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()

def test_bank_cards_display(driver):
    driver.get("http://localhost:3000/")
    
    go_to_lab = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "a.feature-link[href='/automation-lab/cards']"))
    )
    go_to_lab.click()
    
    load_button = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".trigger-btn"))
    )
    load_button.click()
    
    cards_css = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "div"))
    )
    assert cards_css.is_displayed()
    
    cards_xpath = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.XPATH, "//div"))
    )
    assert cards_xpath.is_displayed()
    
    driver.save_screenshot("screenshot_cards_displayed.png")
