import os
from twilio.rest import Client

account_sid = "ACc4c3e4740eaa7830d349c0801a71db41"
auth_token = "01970b06346dd564920b322bcc6f0200"

client = Client(account_sid, auth_token)

client.messages.create(
    to="+17176174482",
    from_="+16692425356",
    body="Hi there"
)

