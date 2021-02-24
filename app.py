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
    return render_template('index.html', url=url)

@app.route('/callback/bungie')#on return from auth
def bungie_callback():
    url = AUTH_URL
    code = request.args.get('code')#gets the auth code
    access_code = code
    access_token = apiManager.get_token(code)#requests token to finalize auth
    for vendor in keys.VENDORS_ID:#for each vendor
        for character in keys.CHARATERS_ID:#for each class
            vendorSales = apiManager.get_vendor_info(vendor,character,access_token)#gets the items stats
            inforParser.parse_items(vendorSales,vendor,character)#parse the info from the sales of the vendor
    
    return render_template('index.html', url=url)


    





if __name__ == '__main__':
    app.run(ssl_context=('cert.pem', 'key.pem'))