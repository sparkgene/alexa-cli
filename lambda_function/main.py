# -*- coding: utf-8 -*-
import os

def lambda_handler(event, context):

    if event['request']['type'] == "IntentRequest":
        return on_intent(event['request'], event["session"])
    elif event['request']['type'] == "SessionEndedRequest":
        return return_cancel()

    return on_launch()


def on_launch():
    print("on_launch")
    return return_hello()

def on_intent(request, session):
    print("on_intent")
    intent_name = request['intent']['name']
    print("intent name: {}".format(intent_name))

    if intent_name == "ImHomeIntent":
        return return_question()
    elif intent_name == "HungryIntent":
        return return_eat()
    elif intent_name == "BathIntent":
        return return_bath()
    elif intent_name == "AMAZON.StopIntent":
        return return_stop()

    return return_hello()

def return_hello():
    data = {
        "title": "ご主人様、こんにちわ。",
        "speech": "こんにちわ、ご主人様。私はご主人様に使える執事です。「ただいま」と話しかけてみて下さい。",
        "reprompt": "「ただいま」と話しかけてみて下さい。",
        "close_session": False
    }
    return build_speechlet_response(data)

def return_question():
    data = {
        "title": "おかえりなさいませ、ご主人様。",
        "speech": "おかえりなさいませ、ご主人様。お食事にしますか？ それとも、お風呂にしますか？",
        "reprompt": "お食事にしますか、お風呂にしますか？",
        "close_session": False
    }

    return build_speechlet_response(data)

def return_bath():
    data = {
        "title": "お風呂ですね。",
        "speech": "お風呂ですね。すぐ用意しますので、くつろいでおまちになってくださいね。",
        "reprompt": None,
        "close_session": True
    }

    return build_speechlet_response(data)

def return_eat():
    data = {
        "title": "お食事ですね。",
        "speech": "お食事ですね。今日はどんな料理が食べたいですか？",
        "reprompt": "今日はどんな料理が食べたいですか？",
        "close_session": False
    }

    return build_speechlet_response(data)

def return_stop():
    data = {
        "title": "さようなら",
        "speech": "いつでも執事にお申し付け下さいね。",
        "reprompt": None,
        "close_session": True
    }

    return build_speechlet_response(data)

def build_speechlet_response(data):

    return_message = {
        "outputSpeech": {
            "type": "PlainText",
            "text": data["speech"]
        },
        "card": {
            "type": "Simple",
            "title": data["title"],
            "content": data["speech"]
        },
        "shouldEndSession": data["close_session"]
    }
    if data["reprompt"] is not None:
        return_message["reprompt"] = {
            "outputSpeech": {
                "type": "PlainText",
                "text": data["reprompt"]
            }            
        }

    return build_response(return_message)

def build_response(speechlet_response):
    response = {
        'version': '1.0',
        'response': speechlet_response
    }
    print(response)
    return response
