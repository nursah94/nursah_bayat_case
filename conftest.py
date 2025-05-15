import pytest
from utils.driver_factory import get_driver

@pytest.fixture
def driver(request):
    browser_name = request.config.getoption("--browser", default="chrome")
    
    driver = get_driver(browser_name)
    driver.maximize_window()
    
    yield driver
    
    driver.quit()

def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome", help="Choose browser: chrome or firefox"
    )
