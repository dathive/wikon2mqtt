import os
from dotenv import load_dotenv

load_dotenv()

MQTT_BROKER = os.getenv('MQTT_BROKER')
MQTT_PORT = int(os.getenv('MQTT_PORT'))
MQTT_TOPIC = os.getenv('MQTT_TOPIC')
SELENIUM_URL = os.getenv('SELENIUM_URL')
WIKON_URL = os.getenv('WIKON_URL')
WIKON_USERNAME = os.getenv('WIKON_USERNAME')
WIKON_PASSWORD = os.getenv('WIKON_PASSWORD')
