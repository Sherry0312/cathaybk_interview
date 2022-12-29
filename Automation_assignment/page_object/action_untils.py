from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ActionUtils:

    def __init__(self, driver):
        self.driver = driver
        self.screenshot_list = []

    def find_presence_elem(self, locator, timeout=10):
        elem = WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
        return elem

    def find_clickable_elem(self, locator, timeout=10):
        elem = WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))
        return elem

    def find_presence_elements(self, locator, timeout=10):
        elem = WebDriverWait(self.driver, timeout).until((EC.presence_of_all_elements_located(locator)))
        return elem

    def save_the_screenshot(self, filename):
        self.driver.get_screenshot_as_file(f"./Screenshot/{filename}.png")

    def get_the_screenshot_list(self, number):
        self.screenshot_list.append(self.driver.get_screenshot_as_file(f"./Screenshot/Screenshot_{number}.png"))
        return self.screenshot_list
