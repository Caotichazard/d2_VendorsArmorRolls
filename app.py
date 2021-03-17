from flask import Flask, render_template, request
from flask_script import Manager
from flask_bootstrap import Bootstrap
import requests
import base64
import json
import keys
import itens
import apiManager
import inforParser
import storer
import tw

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'

manager = Manager(app)
bootstrap = Bootstrap(app)
#https://script.google.com/macros/s/AKfycbxe7UjhMRHi-VKOp2xT_-K96zqiaE6PvsMb4yKfF3JUfl_JYBg/exec

AUTH_URL = "https://www.bungie.net/en/OAuth/Authorize?client_id="+ keys.CLIENT_ID +"&response_type=code"



oauth_session = requests.Session()

@app.route('/')
@app.route('/index')
def index():
    url = AUTH_URL#url to start auth
    urlTw = "/postTweets"
    return render_template('index.html', url=url,urlTw=urlTw)

@app.route('/callback/bungie')#on return from auth
def bungie_callback():
    url = AUTH_URL
    urlTw = "/postTweets"
    code = request.args.get('code')#gets the auth code
    access_code = code
    access_token = apiManager.get_token(code)#requests token to finalize auth
    inforParser.get_data_info(access_token)
    
    return render_template('index.html', url=url,urlTw=urlTw)

@app.route('/postTweets')
def postTweets():
    url = AUTH_URL
    urlTw = "/postTweets"
    print("A")
    data = storer.get_info_from_file(storer.get_file_name())
    tweets = inforParser.prepare_tweets(data)
    tw.tweet_info(tweets)
    print(tweets)
    return render_template('index.html', url=url,urlTw=urlTw)





if __name__ == '__main__':
    app.run(ssl_context=('cert.pem', 'key.pem'))