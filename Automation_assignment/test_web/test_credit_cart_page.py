import time


def test_credit_card_page(credit_card_view):
    # locate in the home page
    credit_card_view.check_icon_display()

    # Get the Home View screen shoot
    credit_card_view.save_the_screenshot("Home_view")

    # Click menu icon
    credit_card_view.click_menu_icon()

    # Click product introduce icon
    credit_card_view.click_product_intro_icon()

    # Click Credit card branch
    credit_card_view.click_credit_card_branch()

    # Check Credit card list len
    list_len = credit_card_view.get_credit_card_list_len()
    assert list_len == 8
    time.sleep(2)
    credit_card_view.save_the_screenshot("Credit_card_list")

    # Click Card introduce
    credit_card_view.click_card_introduce()

    # Locate on the stop sending card section
    credit_card_view.locate_stop_send_card()

    # Compare the stop sending card screenshot amount
    card_amount = credit_card_view.check_the_stop_sending_card_amount()
    screenshot_amount = credit_card_view.get_the_card_screenshot_list_amount()
    assert card_amount == screenshot_amount
