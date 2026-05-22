import os
import allure
from allure_commons.types import AttachmentType
from datetime import datetime


def take_screenshot(driver, name):

    screenshots_dir = "screenshots"

    if not os.path.exists(screenshots_dir):
        os.makedirs(screenshots_dir)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    file_path = f"{screenshots_dir}/{name}_{timestamp}.png"

    driver.save_screenshot(file_path)

    # Attach Screenshot To Allure Report
    allure.attach.file(
        file_path,
        name=name,
        attachment_type=AttachmentType.PNG
    )

    print(f"Screenshot Saved: {file_path}")