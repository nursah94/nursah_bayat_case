from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage
from config import QA_CAREERS_URL
from selenium.webdriver.common.action_chains import ActionChains


class QAJobsPage(BasePage):
    SEE_ALL_JOBS = (By.LINK_TEXT, "See all QA jobs")
    VIEW_ROLE_BUTTON = (By.XPATH, "//a[contains(text(),'View Role')]")
    FILTER_LOC_BTN = (By.ID, "select2-filter-by-location-container")
    FILTER_DEPT_BTN = (By.ID, "select2-filter-by-department-container")  
    FILTER_LOC = (By.XPATH, "//li[contains(@id, 'select2-filter-by-location-result') and contains(text(), '{}')]")
    POSITION_CARDS = (By.CLASS_NAME, "position-list-item")
    POSITION_DEPT = (By.CLASS_NAME, "position-department")
    POSITION_LOC = (By.CLASS_NAME, "position-location")

    def go_to_qa_careers_page(self):
        self.driver.get(QA_CAREERS_URL)

    def click_see_all_qa_jobs(self):
        self.click(self.SEE_ALL_JOBS)

    def filter_jobs(self, location, department):

        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.text_to_be_present_in_element(self.FILTER_DEPT_BTN, department))

        self.click(self.FILTER_LOC_BTN)
        self.click(self.FILTER_LOC, location)


    def verify_job_list(self, expected_loc, expected_dept):
        
        self.driver.execute_script("window.scrollBy(0, 500);")
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located(self.POSITION_CARDS))

        assert self.is_visible((By.ID, "jobs-list")), "Job list is not visible on the page."

        job_items = self.find_elements(self.POSITION_CARDS)

        for job in job_items:
            dept = job.find_element(*self.POSITION_DEPT).text.strip()
            loc = job.find_element(*self.POSITION_LOC).text.strip()

            assert dept == expected_dept, f"Department does not macth! expected: '{expected_dept}', Actual: '{dept}'"
            assert loc == expected_loc, f"Location does not macth! expected: '{expected_loc}', Actual: '{loc}'"

    def click_view_role(self):
        job_items = self.find_elements(self.POSITION_CARDS)
        assert job_items, "There is no Job item"

        first_job = job_items[0]

        actions = ActionChains(self.driver)
        actions.move_to_element(first_job).perform()

        view_button = WebDriverWait(first_job, 10).until(
            EC.element_to_be_clickable((By.XPATH, ".//a[contains(text(),'View Role')]"))
        )

        original_window = self.driver.current_window_handle
        view_button.click()

        WebDriverWait(self.driver, 10).until(lambda d: len(d.window_handles) > 1)
        
        new_window = [window for window in self.driver.window_handles if window != original_window][0]
        self.driver.switch_to.window(new_window)

        assert "lever.co" in self.driver.current_url, "New page does not have'lever.co'."