from twilio.rest import Client 
import config


# client making an object of the class client 
client = Client(config.account_sid, config.auth_token)

#Using the object to call the function associated with the class 
message = client.messages.create(
    to = +447424700497,
    from_ = +19015099892,
    body = "Hello, my name is Ola."
)

print(message.sid)

