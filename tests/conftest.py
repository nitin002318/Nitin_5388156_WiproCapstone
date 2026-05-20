import os
import allure
import pytest


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield
    report = outcome.get_result()

    if report.when == "call":

        screenshot_folder = "screenshots"

        if os.path.exists(screenshot_folder):

            files = [
                os.path.join(screenshot_folder, f)
                for f in os.listdir(screenshot_folder)
                if f.endswith(".png")
            ]

            if files:
                latest_file = max(files, key=os.path.getctime)

                with open(latest_file, "rb") as f:
                    allure.attach(
                        f.read(),
                        name=os.path.basename(latest_file),
                        attachment_type=allure.attachment_type.PNG
                    )

        # Attach logs
        log_file = "logs/test.log"

        if os.path.exists(log_file):
            with open(log_file, "r") as f:
                allure.attach(
                    f.read(),
                    name="Test Logs",
                    attachment_type=allure.attachment_type.TEXT
                )