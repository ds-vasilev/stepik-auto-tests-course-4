from selenium.webdriver.common.by import By
from .base_page import BasePage
from .locators import ProductPageLocators


!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!ВСЕ НАХУЙ ПОМЕНЯТЬ

class ProductPage(BasePage):
    def guest_can_add_product_to_basket(self):
        link = self.browser.find_element(*ProductPageLocators.AD_TO_BASKET)
        self.should_be_login_url()
