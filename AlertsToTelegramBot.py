from __future__ import print_function
from botocore.vendored import requests


BOT_ID = "bot1111111110:Aasdfasfe34y_sdfsf2s-JG4asdf3g3F3KV8"
CHAT_ID = "-156541124435223"
API_ENDPOINT = "https://api.telegram.org/%s/sendMessage" % BOT_ID



def lambda_handler(event,context):
    message = str(event["detail"]["title"])

    try:
      requests.get(API_ENDPOINT + "?chat_id=" + CHAT_ID + "&parse_mode=Markdown&text=" + message)
    except requests.exceptions.RequestException as e:  # This is the correct syntax
        raise SystemExit(e)

