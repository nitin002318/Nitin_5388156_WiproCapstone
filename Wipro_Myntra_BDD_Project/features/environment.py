import os
import allure

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

from utils.logger import get_logger

logger = get_logger()

# Screenshot folder
if not os.path.exists("screenshots"):
    os.makedirs("screenshots")


def before_scenario(context, scenario):

    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")

    context.driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

    logger.info(f"Starting Scenario: {scenario.name}")


def after_step(context, step):

    # Screenshot for every step
    screenshot_name = step.name.replace(" ", "_") + ".png"

    screenshot_path = os.path.join(
        "screenshots",
        screenshot_name
    )

    context.driver.save_screenshot(screenshot_path)

    allure.attach.file(
        screenshot_path,
        name=step.name,
        attachment_type=allure.attachment_type.PNG
    )


def after_scenario(context, scenario):

    if scenario.status == "failed":

        logger.error(f"Scenario Failed: {scenario.name}")

    else:

        logger.info(f"Scenario Passed: {scenario.name}")

    context.driver.quit()