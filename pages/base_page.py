from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

class BasePage:
    COOKIE_ACCEPT_BTN = (By.ID, "wt-cli-accept-all-btn")
    NOTIFICATION_CLOSE_BTN = (By.CLASS_NAME, "notification-close")
    POPUP_CLOSE_BTN = (By.ID, "ins-close-button")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def find_element(self, locator):
        return self.driver.find_element(*locator)

    def find_elements(self, locator):
        return self.driver.find_elements(*locator)    

    def click(self, locator, *args):
        if args:
            by, path = locator
            path = path.format(*args)
            locator = (by, path)

        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def is_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def get_elements(self, locator):
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    def close_popups(self):
        try:
            cookie_btn = self.driver.find_element(*self.COOKIE_ACCEPT_BTN)
            cookie_btn.click()
        except NoSuchElementException:
            pass 

        try:
            notif_btn = self.driver.find_element(*self.NOTIFICATION_CLOSE_BTN)
            notif_btn.click()
        except NoSuchElementException:
            pass

        try:
            popup_btn = self.driver.find_element(*self.POPUP_CLOSE_BTN)
            popup_btn.click()
        except NoSuchElementException:
            pass