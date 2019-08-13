import os
import string
from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse
from src.summary import getSummary, train_markov, getArticleText, handleSummary

app = Flask(__name__)

# Handle an incoming sms message
@app.route("/sms", methods=['GET', 'POST'])
def incoming_sms():

    # Recieve incomeing message, set to lower, and remove punctuation
    body = request.values.get('Body', None).lower().translate(str.maketrans('','',"""!#$%&'()"*+,./:;<=>?@[]^_`{|}~"""))
    
    # Start response
    resp = MessagingResponse()
    
    # Basic list of greetings and goodbyes
    greetings = ['hello', 'hi', "whats up", 'greetings']
    farewells = ['bye', 'goodbye', "farewell", 'see ya']
    
    # Handle basic calls
    if body == 'what':
        resp.message("""Send any subject, can be a word or phrase, and we will send you a one sentence "summary" on it.""")
    elif body in greetings:
        resp.message("Hi friend! Text 'what' for instructions")
    elif body in farewells:
        resp.message("See you soon!")
    
    # Get the summary mesaage
    else:
        resp.message(handleSummary(body))
    
    # Return message
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=80)
