import time
import logging
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

class WikonScraper:
    def __init__(self, selenium_url, wikon_url, username, password):
        self.selenium_url = selenium_url
        self.wikon_url = wikon_url
        self.username = username
        self.password = password

    def get_data(self):
        options = Options()
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")

        driver = webdriver.Remote(command_executor=self.selenium_url, options=options)
        try:
            driver.get(self.wikon_url)
            time.sleep(5)
            driver.find_element(By.ID, "username").send_keys(self.username)
            driver.find_element(By.ID, "password").send_keys(self.password)
            driver.find_element(By.XPATH, '//*[@id="fm1"]/input[4]').click()
            time.sleep(5)

            tank_level = driver.find_element(By.XPATH, '//*[@id="5622662"]/td[4]/div/div/div').text.split(' ')[0]
            forecast = driver.find_element(By.XPATH, '//*[@id="5622662"]/td[5]').text.split(' ')[0]

            logging.info(f"Scraped tank_level={tank_level}, forecast={forecast}")
            return {'tank_level': tank_level, 'forecast': forecast}
        finally:
            driver.quit()
