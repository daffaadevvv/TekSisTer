from flask import Flask, jsonify, redirect
import feedparser

app = Flask(__name__)

# Function grabs the rss feed headlines (titles) and returns them as a list
def getHeadlines( rss_url ):
    headlines = []
    
    feed = feedparser.parse( rss_url ) 
    for newsitem in feed['items']:
        headlines.append(newsitem['title'])
        headlines.append(newsitem['link'])
    
    return headlines

@app.route('/', methods=['GET'])
def home():
    return '''<h1>Welcome to News Feeder API</h1>
<p>A prototype API for national and international news feed getter.</p>'''

@app.route('/resources/documentation', methods=['GET'])
def documentation():
    return redirect('https://app.swaggerhub.com/apis/daffaadevvv/NewsFeederAPI/1.0.0', code = 303)


@app.route('/resources/news/internasional', methods=['GET'])
def indexinter():

    # A list to hold all headlines
    allinterheadlines = []
    
    # List of RSS feeds that we will fetch and combine
    newsinturls = {
        'rtnews':           'https://www.rt.com/rss/',
        'googlenews':       'https://news.google.com/news/rss/?hl=en&amp;ned=us&amp;gl=US'
    }
    
    # Iterate over the feed urls
    for key,url in newsinturls.items():
        # Call getHeadlines() and combine the returned headlines with allheadlines
        allinterheadlines.extend( getHeadlines( url ) )

    print(allinterheadlines)

    return jsonify(allinterheadlines)

@app.route('/resources/news/dalamnegeri', methods=['GET'])
def indexnat():

    # A list to hold all headlines
    allnatheadlines = []
    
    # List of RSS feeds that we will fetch and combine
    newsnaturls = {
        'republikanews':    'https://www.republika.co.id/rss',
        'detiknews':        'http://rss.detik.com/index.php/detikcom'
    }
    
    # Iterate over the feed urls
    for key,url in newsnaturls.items():
        # Call getHeadlines() and combine the returned headlines with allheadlines
        allnatheadlines.extend( getHeadlines( url ) )

    print(allnatheadlines)

    return jsonify(allnatheadlines)


if __name__ == '__main__':
    app.run(debug = True)