import logging
import schedule
import time

from config import (
    MQTT_BROKER,
    MQTT_PORT,
    MQTT_TOPIC,
    SELENIUM_URL,
    WIKON_URL,
    WIKON_USERNAME,
    WIKON_PASSWORD
)

from wikon import WikonScraper
from mqtt_client import MQTTPublisher

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def processor():
    logging.info("Starting to process Wikon > MQTT")
    print(SELENIUM_URL)
    scraper = WikonScraper(
        selenium_url=SELENIUM_URL,
        wikon_url=WIKON_URL,
        username=WIKON_USERNAME,
        password=WIKON_PASSWORD
    )
    data = scraper.get_data()

    publisher = MQTTPublisher(
        broker=MQTT_BROKER,
        port=MQTT_PORT,
        base_topic=MQTT_TOPIC
    )
    publisher.connect()
    publisher.publish(data)
    publisher.disconnect()

    logging.info("Process completed successfully")

if __name__ == "__main__":
    schedule.every().day.at("09:00").do(processor)
    logging.info("Scheduler active. Waiting for 09:00...")
    while True:
        schedule.run_pending()
        time.sleep(60)
