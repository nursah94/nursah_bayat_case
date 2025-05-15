import os
from datetime import datetime

def take_screenshot(driver, name="screenshot"):
    now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    file_name = f"{name}_{now}.png"
    os.makedirs("screenshots", exist_ok=True)
    driver.save_screenshot(os.path.join("screenshots", file_name))
