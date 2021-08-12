import json
import keys
import requests
import base64


AUTH_URL = "https://www.bungie.net/en/OAuth/Authorize?client_id="+ keys.CLIENT_ID +"&response_type=code"

access_token = ""

def get_token(code):
    
    access_token_url = "https://www.bungie.net/Platform/App/OAuth/Token/"
    dataString = keys.CLIENT_ID +":"+ keys.CLIENT_SECRET
    dataBytes = dataString.encode("utf-8")
    encoded = base64.b64encode(dataBytes)
    
    
    HEADERS = {
        "Authorization":"Basic " + encoded.decode(),
        "Content-Type":"application/x-www-form-urlencoded"
    }
    PAYLOAD = {
        "grant_type":"authorization_code",
        "code": code
    }
    response = requests.post(access_token_url, headers=HEADERS, data=PAYLOAD)
    

    responseJson = response.json()
    access_token = responseJson['access_token']
    refresh_token = responseJson['refresh_token']
    
    
    
    return access_token
    
    

def refresh_token(refresh_token):
    access_token_url = "https://www.bungie.net/Platform/App/OAuth/Token/"
    dataString = keys.CLIENT_ID +":"+ keys.CLIENT_SECRET
    dataBytes = dataString.encode("utf-8")
    encoded = base64.b64encode(dataBytes)
    
    
    HEADERS = {
        "Authorization":"Basic " + encoded.decode(),
        "Content-Type":"application/x-www-form-urlencoded"
    }
    PAYLOAD = {
        "grant_type":"refresh_token",
        "code": refresh_token
    }
    response = requests.post(access_token_url, headers=HEADERS, data=PAYLOAD)
    

    responseJson = response.json()
    access_token = responseJson['access_token']
    refresh_token = responseJson['refresh_token']
    
    
    
    return access_token
    pass

def get_vendor_info(vendorName,charClass,access_token):
    url = "https://www.bungie.net/Platform/Destiny2/"+keys.MEMBERSHIP_TYPE+"/Profile/"+keys.MEMBERSHIP_ID+"/Character/"+keys.CHARATERS_ID[charClass]+"/Vendors/"+keys.VENDORS_ID[vendorName]+"?components=402,304,305"
    
    HEADERS = {
        "Authorization":"Bearer " + access_token,
        "X-API-KEY": keys.API_KEY
    }

    request = requests.get(url, headers=HEADERS)
    response = request.json()
    #print(vendorName)
    #print(json.dumps(response["Response"],indent=1))
    return response["Response"]["itemComponents"]
    

def get_vendors(charClass,access_token):
    url = "https://www.bungie.net/Platform/Destiny2/"+keys.MEMBERSHIP_TYPE+"/Profile/"+keys.MEMBERSHIP_ID+"/Character/"+keys.CHARATERS_ID[charClass]+"/Vendors/"+keys.VENDORS_ID["Ada-1"]+"?components=402,304"
    
    HEADERS = {
        "Authorization":"Bearer " + access_token,
        "X-API-KEY": keys.API_KEY
    }

    request = requests.get(url, headers=HEADERS)
    response = request.json()
    return response