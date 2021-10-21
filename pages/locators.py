from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")


class ProductPageLocators():
    ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    BOOK_NAME = (By.CSS_SELECTOR, ".product_main>h1")                                       #Проверить
    BOOK_NAME_MESENGER = (By.CSS_SELECTOR, ".alert:nth-child(1) .alertinner strong")
    BOOK_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    BOOK_PRICE_BASKETS = (By.CSS_SELECTOR, ".basket-mini >strong")
    BOOK_PRICE_MESENGER = (By.CSS_SELECTOR, ".alert:nth-child(3) .alertinner strong")