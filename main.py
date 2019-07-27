import os
import string
from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse
from summary import getSummary, train_markov, getArticleText, handleSummary

app = Flask(__name__)

@app.route("/sms", methods=['GET', 'POST'])
def incoming_sms():

    # Recieve incomeing message, set to lower, and remove punctuation
    body = request.values.get('Body', None).lower().translate(str.maketrans('','',"""!#$%&'()"*+,./:;<=>?@[]^_`{|}~"""))
    
    # Start response
    resp = MessagingResponse()
    
    # Basic list of greetings and goodbyes
    greetings = ['hello', 'hi', "whats up", 'greetings']
    farewells = ['bye', 'goodbye', "farewell", 'see ya']
    
    if body == 'help':
        resp.message("Type any subject, can be a word or phrase, and we will send you a brief summary.")
    elif body in greetings:
        resp.message("Hi friend! Text 'help' for instructions")
    elif body in farewells:
        resp.message("See you soon!")
    else:
        resp.message(handleSummary(body))

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
