import logging
from paho.mqtt.client import Client, CallbackAPIVersion

class MQTTPublisher:
    def __init__(self, broker, port, base_topic):
        self.broker = broker
        self.port = port
        self.base_topic = base_topic
        self.client = Client(callback_api_version=CallbackAPIVersion.VERSION2)

    def connect(self):
        self.client.connect(self.broker, self.port)
        logging.info(f"Connecté à MQTT {self.broker}:{self.port}")

    def publish(self, data: dict):
        for key, value in data.items():
            topic = self.base_topic + key
            self.client.publish(topic, value, retain=True)
            logging.info(f"Publié sur {topic}: {value}")

    def disconnect(self):
        self.client.disconnect()
        logging.info("Déconnecté du broker MQTT")
