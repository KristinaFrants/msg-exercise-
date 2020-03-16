import os
from twilio.rest import Client

def send_msg(mess):
    account_sid = os.environ.get("KACCOUT_SEED")
    auth_token = os.environ.get("KACCOUNT_TOKEN")
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
            body=mess,
            from_='+12064660581',
            to='+14078666541'
        )

    print(message.sid)