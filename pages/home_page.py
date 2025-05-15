from selenium.webdriver.common.by import By
from .base_page import BasePage
from config import BASE_URL

class HomePage(BasePage):
    COMPANY_MENU = (By.XPATH, "//a[@id='navbarDropdownMenuLink' and contains(text(), 'Company')]")
    CAREERS_LINK = (By.XPATH, "//a[@class='dropdown-sub' and contains(text(), 'Careers')]")

    def load(self):
        self.driver.get(BASE_URL)
        self.close_popups()
        assert "Insider" in self.driver.title, "Title is not visible!"

    def go_to_careers(self):
        self.click(self.COMPANY_MENU)
        self.click(self.CAREERS_LINK)