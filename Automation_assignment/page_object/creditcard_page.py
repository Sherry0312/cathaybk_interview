import logging
import time

from selenium.webdriver.common.by import By
from page_object.action_untils import ActionUtils


class CreditCardView(ActionUtils):
    icon_locator = (By.CSS_SELECTOR, "#lnk_Link")
    menu_icon_locator = (By.CLASS_NAME, "cubre-o-header__burger")
    product_intro_locator = (By.XPATH, "//div[text()='產品介紹']")
    credit_card_branch_locator = (By.XPATH, "//div[text()='信用卡']")
    credit_card_list_locator = (By.XPATH, "//div[text()='信用卡']/following-sibling::a")
    card_intro_locator = (By.XPATH, "//a[text()='卡片介紹']")
    stop_send_card_locator = (By.XPATH, "//section[@data-anchor-block='blockname06']")
    switch_btn_locator = (By.CSS_SELECTOR, ".-iconTitle:nth-child(7) .swiper-pagination-bullet")

    def check_icon_display(self):
        self.find_presence_elem(self.icon_locator)

    def click_menu_icon(self):
        self.find_clickable_elem(self.menu_icon_locator).click()

    def click_product_intro_icon(self):
        self.find_clickable_elem(self.product_intro_locator).click()

    def click_credit_card_branch(self):
        self.find_clickable_elem(self.credit_card_branch_locator).click()

    def get_credit_card_list_len(self):
        list_len = len(self.find_presence_elements(self.credit_card_list_locator))
        logging.info(f"Credit card list length is : {list_len}")
        return list_len

    def click_card_introduce(self):
        self.find_clickable_elem(self.card_intro_locator).click()

    def locate_stop_send_card(self):
        self.find_presence_elem(self.stop_send_card_locator).click()

    def check_the_stop_sending_card_amount(self):
        btn_list = self.find_presence_elements(self.switch_btn_locator)
        logging.info(f"It has/have {len(btn_list)} stop sending credict card(s)")
        return len(btn_list)

    def get_the_card_screenshot_list_amount(self):
        screenshot_list = []
        number = 0
        btn_list = self.find_presence_elements(self.switch_btn_locator)
        for btn in btn_list:
            btn.click()
            number += 1
            time.sleep(1)
            screenshot_list = self.get_the_screenshot_list(number)
        logging.info(f"It has/have {len(screenshot_list)} screenshot(s)")
        return len(screenshot_list)
