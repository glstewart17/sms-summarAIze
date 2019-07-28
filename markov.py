# Trains the markov chain using the article
def train_markov(article):
    
    # Set text to a list split from the article
    text = article.lower().split()
    chain = {}

    # Set i to 2, seeing as we will search two back
    i = 2

    # While i is less than the length of the list of text
    while i < len(text):
        try:
            
            # Set the key to the last two pieces of text with a space inbetween
            key = text[i - 2] + " " + text[i - 1]
            
            # If punctuation is inthe key, increase i by one and continue
            if "?" in key or "." in key or "!" in key:
                i += 1
                continue
            
            # If key in chain add word to the value list 
            if key in chain:
                chain[key] += [text[i]]

            # Set the value to this key
            else:
                chain[key] = [text[i]]
        
        # Should not occur, but just in case
        except:
            print("FAILED")
        
        # Increase i by one
        i += 1

    # Return chain
    return chain