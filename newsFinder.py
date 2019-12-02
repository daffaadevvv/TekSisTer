from flask import Flask
import feedparser

app = Flask(__name__)


@app.route('/')
def index():
    try:
        return 'this is newsfinder api by daffa alfaridzi'
    except Exception as e:
        raise e

# Function grabs the rss feed headlines (titles) and returns them as a list
def getHeadlines(rss_url):
    try:
        listLink = []
        
        feed = feedparser.parse(rss_url)
        for newsitem in feed['items']:
            listLink.append(newsitem['link'])

        return listLink
    except Exception as e:
        raise e

@app.route('/dalamNegeri/<keyword>')
def dalamNegeri(keyword):
    try:
        listLink = getHeadlines('https://www.republika.co.id/rss')
        
        phrase = keyword.lower()
        
        result = {
            'phrase': phrase,
            'link': 'Link tidak ditemukan, coba keyword lain'
        }

        for link in listLink:
            if phrase in link.lower():
                result['link'] = link
                break

        return result
    except Exception as e:
        raise e

if __name__ == '__main__':
    app.run(threaded = True)