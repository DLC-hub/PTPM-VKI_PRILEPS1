import unittest
from selenium import webdriver
from pages.calculator_page import CalculatorPage


class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.globalsqa.com/angularJs-protractor/SimpleCalculator/")
        self.page = CalculatorPage(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test_plus(self):
        self.page.input_first(5)
        self.page.input_second(7)
        self.page.select_op("+")
        self.page.click_go()
        self.assertEqual(self.page.get_result(), "12")

    def test_minus(self):
        self.page.input_first(10)
        self.page.input_second(4)
        self.page.select_op("-")
        self.page.click_go()
        self.assertEqual(self.page.get_result(), "6")

    def test_multiply(self):
        self.page.input_first(3)
        self.page.input_second(5)
        self.page.select_op("*")
        self.page.click_go()
        self.assertEqual(self.page.get_result(), "15")

    def test_divide(self):
        self.page.input_first(20)
        self.page.input_second(5)
        self.page.select_op("/")
        self.page.click_go()
        self.assertEqual(self.page.get_result(), "4")

    def test_modulo(self):
        self.page.input_first(10)
        self.page.input_second(3)
        self.page.select_op("%")
        self.page.click_go()
        self.assertEqual(self.page.get_result(), "1")

    def test_negative(self):
        self.page.input_first(-5)
        self.page.input_second(-5)
        self.page.select_op("*")
        self.page.click_go()
        self.assertEqual(self.page.get_result(), "25")

    def test_divide_by_zero(self):
        self.page.input_first(5)
        self.page.input_second(0)
        self.page.select_op("/")
        self.page.click_go()
        self.assertEqual(self.page.get_result(), "Infinity")


if __name__ == '__main__':
    unittest.main()