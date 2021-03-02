import itens
import apiManager
import keys
import json
import tw
import storer

def parse_items(info,vendor,character):
    item_indexes = itens.item_index_dict[vendor][character]
    items_info = {}
    notable = 0
    items_info["items"] = {}
    for item,index in item_indexes.items():
        item_stats = info[index]["stats"]
        temp = {}
        stat_total = 0
        for stat_hash,stat in itens.armor_stats.items():
            stat_value = item_stats[stat_hash]["value"]
            stat_total += stat_value
            temp[stat] = stat_value
        temp["stat_total"] = stat_total
        item_judged = judge_item(temp)
        if item_judged["is_notable"]:
            notable += 1
        items_info["items"][item] = item_judged
    items_info["notable_rolls"] = str(notable)
    
    return items_info

def get_all_info(access_token):
    all_gear = {}
    all_classes_notable = 0
    for character,char_id in keys.CHARATERS_ID.items():#for each class
        all_gear[character] = {}
        notable = 0
        for vendor,vendor_id in keys.VENDORS_ID.items():#for each vendor
            vendorSales = apiManager.get_vendor_info(vendor,character,access_token)#gets the items stats
            all_gear[character][vendor] = parse_items(vendorSales,vendor,character)#parse the info from the sales of the vendor
            notable += int(all_gear[character][vendor]["notable_rolls"])
        all_gear[character]["total_notable_rolls"] = str(notable)
        all_classes_notable += notable
    all_gear["all_notable_rolls"] = str(all_classes_notable)
    #print(json.dumps(all_gear, indent =2))
    return all_gear

def get_tweets_info(access_token):
    all_info = get_all_info(access_token)
    tweets = prepare_tweets(all_info)
    
    tw.tweet_info(tweets)
    storer.store_info(all_info)

    
def judge_item(item):
    if item["stat_total"] >=58:
        item["is_notable"] = True
    elif item["Recovery"] >= 26 or item["Resilience"] >= 26 or item["Mobility"] >= 26 or item["Discipline"] >= 26 or item["Intellect"] >= 26 or item["Strength"] >= 26:
        item["is_notable"] = True
    else:
        item["is_notable"] = False
    
    return item

def prepare_tweets(all_info):
    tweets = {}

    overall_tweet = overall_tweet_prep(all_info)
    tweets["overall"] = overall_tweet
    for char, char_id in keys.CHARATERS_ID.items():
        tweets[char] = char_thread_prep(all_info[char],char)
    #print(json.dumps(tweets, indent =2))
    return tweets
    #char_thread_prep(all_info["hunter"],"hunter")
    #char_thread_prep(all_info["warlock"],"warlock")
    

def overall_tweet_prep(all_info):
    overall_tweet = "This week the number of notable rolls are\n" + all_info["all_notable_rolls"] + "\n"
    overall_tweet += "Total notable rolls per class:\n" 
    overall_tweet += "Hunters: " + all_info["hunter"]["total_notable_rolls"] + "\n"
    overall_tweet += "Titans: " + all_info["titan"]["total_notable_rolls"] + "\n"
    overall_tweet += "Warlocks: " + all_info["warlock"]["total_notable_rolls"] + "\n"
    overall_tweet += "\nCheck the following threads(one per class) for info on each roll"
    overall_tweet += "\nAnd don't forget to grab any rolls you need!"
    return overall_tweet

def char_thread_prep(char_info,char_class):
    tweets = []
    if char_info["total_notable_rolls"] == "0":
        
        tweet = "Sadly the RNG gods haven't graced the "
        if char_class == "warlock":
            tweet += "Warlocks, go back to reading those books "
        elif char_class == "titan":
            tweet += "Titans, go back to punching stuff "
        else:
            tweet += "Hunters, go back to shatterdiving "
        
        tweet +="and come back next week!"
        tweets.append(tweet)
        return tweets
    else:
        notable_rolls = {}
        for vendor,vendor_id in keys.VENDORS_ID.items():
            for item,info in char_info[vendor]["items"].items():
                if info["is_notable"]:
                    tweet = "This week " + vendor + " is selling a notable " + item + " for the "
                    if char_class == "warlock":
                        tweet += "Warlocks"
                    elif char_class == "titan":
                        tweet += "Titans"
                    else:
                        tweet += "Hunters"
                    tweet += " with the following stats:\n\n"

                    tweet += "Mobility " + str(info["Mobility"]) + '\n'
                    tweet += "Resilience " + str(info["Resilience"]) + '\n'
                    tweet += "Recovery " + str(info["Recovery"]) + '\n'
                    tweet += "Discipline " + str(info["Discipline"]) + '\n'
                    tweet += "Intellect " + str(info["Intellect"]) + '\n'
                    tweet += "Strength " + str(info["Strength"]) + '\n'
                    tweets.append(tweet)
        return tweets



#make a rating system
def judge_item_experiment(item,char):
    grade = 0
    if item["stat_total"] >=60:
        grade += 2.0
    if char == "titan":
        if item["Recovery"] >= 18:
            grade += 1.0
        if item["Resilience"] >= 18:
            grade += 1.0
    elif char == "warlock":
        if item["Recovery"] >= 18:
            grade += 2.0
        if item["Resilience"] >= 18:
            grade += 0.5
    else: 
        if item["Recovery"] >= 18:
            grade += 1.0
        if item["Resilience"] >= 18:
            grade += 0.5