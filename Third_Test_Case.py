from global_settings.base_test import BaseTest
from selenium.webdriver.support import expected_conditions as EC


class third_test(BaseTest):
    def test_new(self):
        self.wait.until(EC.element_to_be_clickable(self.all_locators['thirdexample'])).click()
        self.wait.until(EC.element_to_be_clickable(self.all_locators['thirdexample'])).setValue()