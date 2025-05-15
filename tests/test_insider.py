import pytest
from pages.home_page import HomePage
from pages.careers_page import CareersPage
from pages.qa_jobs_page import QAJobsPage
from utils.screenshot import take_screenshot

def test_insider_qa_jobs(driver):
    try:
        # Step 1: Open home page
        home = HomePage(driver)
        home.load()

        # Step 2: Go to careers
        home.go_to_careers()
        careers = CareersPage(driver)
        careers.verify_blocks()
        
        # Step 3: Go to QA jobs
        qa_page = QAJobsPage(driver)
        qa_page.go_to_qa_careers_page()
        qa_page.click_see_all_qa_jobs()
        qa_page.filter_jobs("Istanbul, Turkiye", "Quality Assurance")
        qa_page.verify_job_list("Istanbul, Turkiye", "Quality Assurance")

        # Step 5: View role and verify redirection
        qa_page.click_view_role()

    except Exception as e:
        take_screenshot(driver, "test_failure")
        raise e