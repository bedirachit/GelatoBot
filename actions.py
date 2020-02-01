from typing import Dict, Text, Any, List, Union, Optional

from rasa_sdk import Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction
from RasaBot import webhooks


class OrderForm(FormAction):
    """Example of a custom form action"""

    def name(self) -> Text:
        """Unique identifier of the form"""

        return "order_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        return ["order_id"]

    @staticmethod
    def is_int(string: Text) -> bool:
        """Check if a string is an integer"""

        try:
            int(string)
            return True
        except ValueError:
            return False

    def validate_order_id(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validate num_people value."""

        if self.is_int(value) and int(value) > 0:
            return {"order_id": value}
        else:
            dispatcher.utter_message(template="utter_wrong_num_people")
            # validation failed, set slot to None
            return {"order_id": None}

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        """A dictionary to map required slots to
            - an extracted entity
            - intent: value pairs
            - a whole message
            or a list of them, where a first match will be picked"""

        return {
            "order_id": [
                self.from_entity(
                    entity="order_id", intent=["inform", "order_status"]
                ),
                self.from_entity(entity="number"),
            ]
        }

    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        """Define what the form has to do
            after all required slots are filled"""
        order_id = tracker.get_slot("order_id")
        order_details = webhooks.get_order_details(order_id)
        print(order_details)
        if not order_details:
            bot_response = "Having trouble locating your order. Please make sure your order id is correct."
            dispatcher.utter_message(bot_response)
            return []

        if order_details.get("status") == 'dispatched':
            bot_response = "Your order #{} of {} has been dispatched and expected to arrive on {}".\
                format(order_id,order_details["description"], order_details["delivery"][0])
        elif order_details.get("status") == 'delivered':
            bot_response = "Your order #{} of {} has been delivered on {}".\
                format(order_id,order_details["description"], order_details["delivery"][0])
        elif order_details.get("status") == 'production':
            bot_response = "Your order #{} of {} is in production and is yet to be dispatched.".\
                format(order_id,order_details["description"])
        elif order_details.get("status") == 'cancelled':
            bot_response = "Your order #{} of {} is cancelled".\
                format(order_id,order_details["description"])
        else:
            bot_response = "Having trouble locating your order. Please make sure your order id is correct."
        # utter submit template
        dispatcher.utter_message(bot_response)
        return []