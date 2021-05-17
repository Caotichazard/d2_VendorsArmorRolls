from flask import Flask, render_template, request
from flask.templating import render_template_string
from flask_script import Manager
from flask_bootstrap import Bootstrap
import requests
import base64
import json

from requests import api
import keys
import itens
import apiManager
import inforParser
import storer
import tw
import img_gen

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'

manager = Manager(app)
bootstrap = Bootstrap(app)


AUTH_URL = "https://www.bungie.net/en/OAuth/Authorize?client_id="+ keys.CLIENT_ID +"&response_type=code"



oauth_session = requests.Session()

##starting point
@app.route('/')
@app.route('/index')
def index():
    url = AUTH_URL#url to start auth
    urlImg = "/generateImages"
    urlTw = "/postTweets"#url to tweet info
    return render_template('index.html', url=url,urlTw=urlTw,urlImg=urlImg)

@app.route('/callback/bungie')#on return from auth
def bungie_callback():
    url = AUTH_URL
    urlImg = "/generateImages"
    urlTw = "/postTweets"
    print("1")
    code = request.args.get('code')#gets the auth code
    print("1")
    access_code = code
    access_token = apiManager.get_token(code)#requests token to finalize auth
    print("1")
    inforParser.get_data_info(access_token)#gets info
    #print(apiManager.get_vendors("hunter",access_token))
    return render_template('index.html', url=url,urlImg=urlImg,urlTw=urlTw)#sets info to try again


@app.route('/generateImages')
def genImages():
    url = AUTH_URL
    urlTw = "/postTweets"
    urlImg = "/generateImages"
    data = storer.get_info_from_file(storer.get_file_name())
    img_gen.generateImgs(data)
    return render_template('index.html', url=url,urlImg=urlImg,urlTw=urlTw)#sets info to try again


@app.route('/postTweets')#url to post info
def postTweets():
    url = AUTH_URL
    urlTw = "/postTweets"
    urlImg = "/generateImages"
    data = storer.get_info_from_file(storer.get_file_name())
    tweets = inforParser.prepare_tweets(data)
    tw.tweet_info(tweets)
    print(tweets)
    return render_template('index.html', url=url,urlImg=urlImg,urlTw=urlTw)#sets info to try again

@app.route('/titan')
def showTitan():
    data = storer.get_info_from_file(storer.get_file_name())
    html_to_render = img_gen.infoToHtml(data["titan"],'titan')
    img_gen.generateImgs(data)
    return render_template_string(html_to_render)

@app.route('/hunter')
def showHunter():
    data = storer.get_info_from_file(storer.get_file_name())
    html_to_render = img_gen.infoToHtml(data["hunter"],'hunter')
    return render_template_string(html_to_render)

@app.route('/warlock')
def showWarlock():
    data = storer.get_info_from_file(storer.get_file_name())
    html_to_render = img_gen.infoToHtml(data["warlock"],'warlock')
    return render_template_string(html_to_render)



if __name__ == '__main__':
    app.run(ssl_context=('cert.pem', 'key.pem'))