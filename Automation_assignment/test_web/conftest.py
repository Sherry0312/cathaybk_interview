import pytest
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from page_object.creditcard_page import CreditCardView


@pytest.fixture
def driver():
    service = Service(executable_path=ChromeDriverManager().install())
    # Display on the desktop
    # driver = webdriver.Chrome(service=service)
    # driver.set_window_size(400, 750)
    # Headless
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=400x750")
    driver = webdriver.Chrome(service=service, options=chrome_options)

    driver.get("https://www.cathaybk.com.tw/cathaybk/")
    yield driver
    driver.quit()


@pytest.fixture
def credit_card_view(driver):
    return CreditCardView(driver)
