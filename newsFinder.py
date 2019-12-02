from flask import Flask
import feedparser

app = Flask(__name__)


@app.route('/')
def index():
    try:
        return '''<h1>Selamat Datang ke News Feeder API!</h1>
        <h2>A prototype API for national news feed getter.</h2>
        <p> Untuk menggunakan API ini, terdapat 1 endpoint saja, yaitu /dalamnegeri/keyword</p> 
        <p> Cara menggunakan API ini cukup simple : Ganti keyword dengan kata yang Anda ingin cari </p>
        <h3> Terima Kasih! </h3>
        <p><strong> Created by Muhammad Daffa Alfaridzi - 18217013</strong></p>
        '''
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