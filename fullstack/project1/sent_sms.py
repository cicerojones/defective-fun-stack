from twilio.rest import TwilioRestClient

# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "ACae07e1e367fe85d5e7e58e729baef7e8" 
# Test account_sid:
# AC5e2955f322c78dd28ece2104aa9cbda3
# test auth_token:
# adc3c274dab9016c91dc2a8ec7752f3b
# 1 914-825-4758

auth_token = "4a2e023114ed531a464a76a33c9cf5e5"
client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(
    body="Jenny please?! I love you <3",
    to="+19143159072",    # Replace with your phone number
    from_="+19148254758") # Replace with your Twilio number

print message.sid
