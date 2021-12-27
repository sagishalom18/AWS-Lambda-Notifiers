#!/usr/bin/python3.6
import urllib3
import json

http = urllib3.PoolManager()

event["detail"]["title"]
def send_slack_message(event):
    url = "https://hooks.slack.com/services/balaaa/ababasNCU/basdbsdbe3dsSDFSDFsdSDm"
    msg = {
        "channel": "#aws-alerts",
        "username": "AWS-Config",
        "text": event,
        "icon_emoji": ""
    }

    encoded_msg = json.dumps(msg).encode('utf-8')

    resp = http.request('POST', url, body=encoded_msg)
    return {
        "message": msg,
        "status_code": resp.status,
        "response": resp.data
    }


def parse_event_to_msg(event):
        msg = "Event: {} triggered on {}.".format(event['detail-type'], event['resources'][0])
        print (msg)
        return msg
        
        
def lambda_handler(event, context):
    print(event)
    send_slack_message(parse_event_to_msg(event))

