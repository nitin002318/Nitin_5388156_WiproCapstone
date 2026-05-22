import allure

from utils.logger import logger
from utils.screenshot import take_screenshot


# Before Every Scenario
def before_scenario(context, scenario):

    logger.info(f"Starting Scenario: {scenario.name}")


# After Every Step
def after_step(context, step):

    if step.status == "failed":

        logger.error(f"Step Failed: {step.name}")

        screenshot_path = take_screenshot(
            context.driver,
            f"FAILED_{step.name.replace(' ', '_')}"
        )

        # Attach Failed Screenshot
        with open(screenshot_path, "rb") as file:

            allure.attach(
                file.read(),
                name=f"FAILED_{step.name}",
                attachment_type=allure.attachment_type.PNG
            )

    else:
        logger.info(f"Step Passed: {step.name}")


# After Every Scenario
def after_scenario(context, scenario):

    logger.info(f"Completed Scenario: {scenario.name}")

    # Pass Scenario Screenshot
    screenshot_path = take_screenshot(
        context.driver,
        f"PASSED_{scenario.name.replace(' ', '_')}"
    )

    # Attach Pass Screenshot
    with open(screenshot_path, "rb") as file:

        allure.attach(
            file.read(),
            name=f"PASSED_{scenario.name}",
            attachment_type=allure.attachment_type.PNG
        )

    # Close Browser
    if hasattr(context, "driver"):

        context.driver.quit()

        logger.info("Browser Closed")