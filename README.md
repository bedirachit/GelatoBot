# GelatoBot - Order status bot
Gelato order status bot

## :surfer: Introduction
The purpose of this repo is to showcase a contextual AI assistant built with the open source Rasa framework.

## 👷‍ Installation

To install GelatoBot, please clone the repo and run:

```
create virtualenv
pip install rasa==1.7.0

```
This is the only python module requirement.
python 3.6
MongoDB (Default IP and port)
Duckling Server (Default IP and port)

## 🤖 To run GelatoBot:

Install MongoDB server to track/persisit bot conversations

Use `rasa train` to train a model (Currently model training is already done. If further training is required, update the model path in config.properties).

Then, to run, first set up your action server in one terminal window:
```
rasa run actions 
```
In another window, run the duckling server:
```
docker run -p 8000:8000 rasa/duckling
```
In another window, run the bot flask server:
set flask_app=RasaBot
flask run --host=0.0.0.0 

## 🤖 REST Endpoint:

### Request

`POST /GelatoBot/Converse/`

      curl --location --request POST 'http://localhost:5000/GelatoBot/Converse' \
           --header 'Content-Type: application/json' \
           --data-raw '{
                        "userMsg": "Hello",
                        "sessionId": "qqaz-1464-gfddwerwqq-8321"
                     }'

### Response

    {
      "bot_message": [
          {
            "recipient_id": "qqaz-1464-gfddwerwqq-8321",
            "text": "Hello! I am support bot! How can I help?"
          }
        ],
      "success": true
    }

## 🤖 Sample bot conversations:

### Conversation 1
  ```
    User: Hello Bot
    Bot: Hello! I am support bot! How can I help?
    User: My shipment details?
    Bot: Please provide your order id
    User: order id is 13
    Bot: Your order #13 of poster is in production and is yet to be dispatched.
    User: thanks
    Bot: you are welcome :)
  ```
 ### Conversation 2
    
    User: Can you tell me about my shipment details my order id is 11 ?
    Bot: Your order #11 of wall calendar has been delivered on 2019-03-04
    

## 👩‍💻 Overview of the files

`data/core/` - contains stories 

`data/nlu` - contains NLU training data

`RasaBot` - contains custom code, flask server, rasaAgentManager, webhooks

`config.properties` - contains application properties

`domain.yml` - the domain file, including bot response templates

`data` - contains rasa nlu and core training files

`config.yml` - training configurations for the NLU pipeline and policy ensemble


## 🤖 GelatoBot solution limitations and possible improvements:

- In the sample conversations provided, On asking bot about order status, the bot directly responded back with order details. A           customer can have multiple simultaneous pending orders. Ideally the bot should ask about the customer order id or some reference       number before sharing details. Though I already made this change.
- Customer specific session management.
- Can share order images along with the details. If already dispatched, can fetch and share current location of the order from the       logistics partner.
- Possiblity of order cancelling or address change or delivery instructions.


