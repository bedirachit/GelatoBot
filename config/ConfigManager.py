import configparser
import os


class Config():

    def __init__(self):
        pass

    @staticmethod
    def read_config():
        ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
        config = configparser.RawConfigParser()
        configFilePath = os.path.join(os.path.split(ROOT_DIR)[0], 'config.properties')
        config.read(configFilePath)
        return config


ROOT_DIR = os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]
config = Config.read_config()

# Order details Url
get_orders_endpoint = config.get('WebhookUrls', 'URL.getOrderDetails')

# Rasa model path
rasa_model_path = os.path.join(ROOT_DIR, config.get('RasaConfig', 'Rasa.modelPath'))