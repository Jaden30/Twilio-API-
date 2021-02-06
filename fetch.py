import config 
from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException
try:
    client = Client(config.account_sid, config.auth_token)

    fetch = client.messages("SMc3c78a5acff544359984a5ce967cbd46").fetch()

    print(fetch.sid)
except TwilioRestException as Error:
    print(Error)