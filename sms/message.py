from twilio.rest import Client

twilio_account_sid = 'AC658b7d2296fc704180ff900691080c3a'
twilio_auth_token = 'e9869ded06c40e9f97754df11621ce7a'
twilio_number = 12055486810

# sent sms request message
def send_message(phone, name, message, d_name):

    client = Client(twilio_account_sid, twilio_auth_token)

    body = "Hello {0}. {1}. -- From doctor {2}".format(
        name,
        message,
        d_name
    )

    client.messages.create(
        phone,
        from_=twilio_number,
        body=body)
