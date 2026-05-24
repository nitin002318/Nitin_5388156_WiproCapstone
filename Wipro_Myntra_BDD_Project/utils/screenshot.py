import os
from datetime import datetime


def take_screenshot(driver, scenario_name):

    folder_path = "reports/screenshots"

    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    timestamp = datetime.now().strftime(
        "%Y%m%d_%H%M%S"
    )

    file_name = f"{scenario_name}_{timestamp}.png"

    screenshot_path = os.path.join(
        folder_path,
        file_name
    )

    driver.save_screenshot(screenshot_path)