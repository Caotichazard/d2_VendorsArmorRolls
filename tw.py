import keys

access_token = keys.TWITTER_KEYS["access_token"]
access_token_secret = keys.TWITTER_KEYS["access_token_secret"]
consumer_key = keys.TWITTER_KEYS["consumer_key"]
consumer_secret = keys.TWITTER_KEYS["consumer_secret"]

import tweepy

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)


def get_last_tweet():
    tweet = api.user_timeline(id = api.me().id, count = 1)[0]
    return tweet


def tweet_info(info):
    images = ('titan.png', 'hunter.png','warlock.png')
    media_ids = [api.media_upload(i).media_id_string  for i in images] 
    print(media_ids)
    
    tweet_head = api.update_status(status = info["overall"], media_ids=media_ids)
    #for char, char_id in keys.CHARATERS_ID.items():
        #cur_head = tweet_head
        #for roll in info[char]:
            #cur_head = api.update_status(status = roll,in_reply_to_status_id = cur_head.id_str)
            
