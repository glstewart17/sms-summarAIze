import wikipedia
import re

# Get the article using the wikipedia library
def getArticleText(article):
    
    # Handle incoming pages, joining if there are more than one
    try:
        if 'en.wikipedia.org' in article:
            while '/' in article:
                article = article[article.find('/') + 1:]
                page = wikipedia.page(" ".join(article.split("_")))
        else:
            page = wikipedia.page(article)
    
    # Otherwise, return None
    except:
        return None

    # Define content using page
    content = page.content
    contentlist = content.split('== See also ==')
    content = ''.join(contentlist[0])
    content = re.sub('==','', content)
    content = re.sub('===','', content)
    content = re.sub('=','', content)

    # Return content
    return content
