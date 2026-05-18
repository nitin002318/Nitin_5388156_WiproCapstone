import time

from utils.driver_setup import get_driver
from pages.men_page import MenPage
from utils.logger import logger

def test_men_menu():

    logger.info("Launching Myntra Website")

    driver = get_driver()

    men = MenPage(driver)

    logger.info("Hovering on MEN menu")

    men.hover_on_men()

    time.sleep(3)

    logger.info("MEN menu opened successfully")

    driver.quit()