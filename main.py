import os
import string
from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/sms", methods=['GET', 'POST'])
def incoming_sms():

    # Recieve incomeing message and set to lower
    body = request.values.get('Body', None).lower()

    # Remove punctuation
    body.translate(None, string.punctuation)

    # Start response
    resp = MessagingResponse()
    
    # Basic list of greetings and goodbyes
    greetings = ['hello', 'hi', "whats up", 'greetings']
    farewells = ['bye', 'goodbye', "farewell", 'see ya']
    
    if body == 'help':
        resp.message("Hi friend! Text 'help' for instructions")
    elif body in greetings:
        resp.message("Hi friend! Text 'help' for instructions")
    elif body in farewells:
        resp.message("See you soon!")

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)