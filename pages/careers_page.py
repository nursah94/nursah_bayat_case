from selenium.webdriver.common.by import By
from .base_page import BasePage

class CareersPage(BasePage):
    PAGE = (By.ID, "page-head")
    LOCATIONS = (By.ID, "career-our-location")
    TEAMS = (By.ID, "career-find-our-calling")
    LIFE_AT_INSIDER = (By.XPATH, "//*[contains(text(), 'Life at Insider')]")

    def verify_blocks(self):
        assert self.is_visible(self.PAGE), "'Page' is not visible"
        assert self.is_visible(self.LOCATIONS), "'Locations' is not visible"
        assert self.is_visible(self.TEAMS), "'Teams' is not visible"
        assert self.is_visible(self.LIFE_AT_INSIDER), "'Life at Insider' is not visible"
   
