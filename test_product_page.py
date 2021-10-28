from pages.product_page import ProductPage

link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/?promo=newYear"

def test_guest_can_add_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    book_name = page.get_book_name()
    book_price = page.get_book_price()
    page.compare_book_name_in_basket_and_in_cataloge(book_name)
    page.compare_book_price_in_basket_and_in_cataloge(book_price)

    time.sleep(3)