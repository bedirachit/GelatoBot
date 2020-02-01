## happy path
* greet
    - utter_greet
* order_status
    - order_form
    - form{"name": "order_form"}
    - form{"name": null}
* thankyou
    - utter_noworries

## unhappy path
* greet
    - utter_greet
* order_status
    - order_form
    - form{"name": "order_form"}
* chitchat
    - utter_chitchat
    - order_form
    - form{"name": null}
* thankyou
    - utter_noworries
        

## very unhappy path
* greet
    - utter_greet
* order_status
    - order_form
    - form{"name": "order_form"}
* chitchat
    - utter_chitchat
    - order_form
* chitchat
    - utter_chitchat
    - order_form
* chitchat
    - utter_chitchat
    - order_form
    - form{"name": null}
* thankyou
    - utter_noworries
    
## stop but continue path
* greet
    - utter_greet
* order_status
    - order_form
    - form{"name": "order_form"}
* stop
    - utter_ask_continue
* affirm
    - order_form
    - form{"name": null}
* thankyou
    - utter_noworries

## stop and really stop path
* greet
    - utter_greet
* order_status
    - order_form
    - form{"name": "order_form"}
* stop
    - utter_ask_continue
* deny
    - action_deactivate_form
    - form{"name": null}

## chitchat stop but continue path
* order_status
    - order_form
    - form{"name": "order_form"}
* chitchat
    - utter_chitchat
    - order_form
* stop
    - utter_ask_continue
* affirm
    - order_form
    - form{"name": null}
* thankyou
    - utter_noworries

## stop but continue and chitchat path
* greet
    - utter_greet
* order_status
    - order_form
    - form{"name": "order_form"}
* stop
    - utter_ask_continue
* affirm
    - order_form
* chitchat
    - utter_chitchat
    - order_form
    - form{"name": null}
* thankyou
    - utter_noworries

## chitchat stop but continue and chitchat path
* greet
    - utter_greet
* order_status
    - order_form
    - form{"name": "order_form"}
* chitchat
    - utter_chitchat
    - order_form
* stop
    - utter_ask_continue
* affirm
    - order_form
* chitchat
    - utter_chitchat
    - order_form
    - form{"name": null}
* thankyou
    - utter_noworries

    
## chitchat, stop and really stop path
* greet
    - utter_greet
* order_status
    - order_form
    - form{"name": "order_form"}
* chitchat
    - utter_chitchat
    - order_form
* stop
    - utter_ask_continue
* deny
    - action_deactivate_form
    - form{"name": null}


## bot challenge
* bot_challenge
  - utter_iamabot