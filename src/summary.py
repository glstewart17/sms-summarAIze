import random
from src.wiki import getArticleText
from src.markov import train_markov

# This function handles the summary
def handleSummary(topic):

    # Get article, will either be an article or None    
    article = getArticleText(topic)

    # If the article is None, return a basic fail statement
    if (article == None):
        return "Failed to find any information on %s." % topic
    
    # Otherwise, return the summary using get summary
    return getSummary(train_markov(article), topic)

# Gets the summary
def getSummary(chain, topic, tries = 1):

    # This inner function gets the next word, using the if no other opiton
    def nextWord(word):
        if word not in chain.keys():
            return 'the'
        else:
            return random.choice(chain[word])

    # If the topic is only one word, start using a key starting with it
    if len(topic.split()) == 1:

        lastWord2 = None

        while lastWord2 != topic:
            startOptions = [s for s in list(chain.keys()) if topic in s]

            string = random.choice(startOptions)
            
            response = string

            lastWord = string.split()[len(string.split()) - 1]
            lastWord2 = string.split()[0]
    
    # Otherwise start with the first two words of the topic
    else:
        topicList = topic.split()

        lastWord = topicList[1]
        lastWord2 = topicList[0]

        response = topicList[0] + " " + topicList[1]

    # Continue until reaching a break point
    while True:

        # If the last two words 
        if lastWord == "the" and lastWord2 == "the":
            if tries == 5:
                return "Failed to form a summary on %s." % topic
            else:
                return getSummary(chain, topic, (tries + 1))

        # Redefine the new lastWord and lastWord2
        lastWord, lastWord2 = nextWord(lastWord2 + " " + lastWord), lastWord

        # If ppunctuation in the new lastword, add it and break
        if "?" in lastWord or "." in lastWord or "!" in lastWord:
            response += " " + lastWord
            break

        # Add a space and then the new lastWord
        response += " " + lastWord
    
    # Return the capitalized version of the sentence.
    return response.capitalize()
