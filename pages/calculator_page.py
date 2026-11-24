from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        self._first = (By.CSS_SELECTOR, "input[ng-model='first']")
        self._second = (By.CSS_SELECTOR, "input[ng-model='second']")
        self._op = (By.CSS_SELECTOR, "select[ng-model='operator']")
        self._btn = (By.XPATH, "//button[text()='Go!']")
        self._result = (By.CSS_SELECTOR, "span[ng-bind='result']")

    def input_first(self, num):
        el = self.driver.find_element(*self._first)
        el.clear()
        el.send_keys(str(num))

    def input_second(self, num):
        el = self.driver.find_element(*self._second)
        el.clear()
        el.send_keys(str(num))

    def select_op(self, operation):
        dropdown = Select(self.driver.find_element(*self._op))
        dropdown.select_by_visible_text(operation)

    def click_go(self):
        self.driver.find_element(*self._btn).click()
        WebDriverWait(self.driver, 3).until(EC.presence_of_element_located(self._result))

    def get_result(self):
        return self.driver.find_element(*self._result).text