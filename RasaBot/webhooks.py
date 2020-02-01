from config import ConfigManager as CM
import requests
import logging
from logs import LogHandler

# setup logging
ErrorLogger = logging.getLogger("ErrorLogs")
InfoLogger = logging.getLogger("InfoLogs")
LogHandler.setup_logging()


def get_order_details(order_id, customer_id=None):
    print(order_id)
    try:
        order_endpoint = CM.get_orders_endpoint
        api_response = requests.get(order_endpoint)
        if api_response.status_code == 200:
            order_data = api_response.json()
            for order in order_data:
                if int(order_id) == order['id']:
                    InfoLogger.info("ORDER DETAILS ::: " + str(order))
                    return order
        return None
    except Exception as e:
        ErrorLogger.error("Something went wrong while fetching order details. " + str(e.args))
        return None
