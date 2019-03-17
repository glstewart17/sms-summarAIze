import wikipedia
import re
import random

def article_text(article):
    try:
        if 'en.wikipedia.org' in article:
            while '/' in article:
                article = article[article.find('/') + 1:]
                page = wikipedia.page(" ".join(article.split("_")))
        else:
            page = wikipedia.page(article)
    except:
        search_result=wikipedia.search(article)
        new_article = input("new article: ")
        article_text(new_article)


    content = page.content


    contentlist = content.split('== See also ==')

    content = ''.join(contentlist[0])

    content = re.sub('==','', content)
    content = re.sub('===','', content)
    content = re.sub('=','', content)

    return content


def train_markov(article):
    text = article.split()

    chain = {}

    for i in range(len(text) - 3):
        try:
            if text[i + 2] not in chain[text[i] + " " + text[i + 1]]:
                chain[text[i] + " " + text[i + 1]] += [text[i + 2]]
        except:
            chain[text[i] + " " + text[i + 1]] = [text[i + 2]]
        if text[i] == "the":
            try:
                chain['the'] += [text[i + 1]]
            except:
                chain['the'] = [text[i + 1]]

    return chain


def summarizer(chain, numS):
    temp1 = numS

    def nextWord(word):
        if word not in chain.keys():
            return 'the'
        else:
            return random.choice(chain[word])

    string = random.choice(list(chain.keys()))
    response = string

    lastWord = string.split()[len(string.split()) - 1]
    lastWord2 = string.split()[0]
    while numS > 0:
        print(response)
        print(numS)
        temp = nextWord(lastWord2 + " " + lastWord)



        if ("?" in temp or "." in temp or "!" in temp) and numS == temp1:
            temp1 = -10
            response = response[:max(response.find('.'), response.find('?'), response.find('!'))]
        elif "?" in temp or "." in temp or "!" in temp:
            numS -= 1
        string = temp
        lastWord2, lastWord = lastWord, temp
        response += " " + temp
    for i in range(len(response)):
        if response[i] in '.?!':
            response = response[:i + 1] + '\n' + response[i + 1:]

    return response