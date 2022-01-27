import tweepy
import re
import requests

#Twitter用定数
BT = "先ほど取得したBearer Token"
CK = "先ほど取得したConsumer Key"
CS = "先ほど取得したConsumer Secret"
AT = "先ほど取得したAccess Token"
ATS = "先ほど取得したAccess Token Secret"

#Switch Bot用定数
token = "前回取得したトークン"
url = "https://api.switch-bot.com/v1.0/devices/前回調べたデバイスID/commands"
h = {"Authorization": token, "Content-Type": "application/json; charset=utf8"}
j = {"command": "turnOn", "parameter": "default", "commandType": "command"}

#自分のTwtterのユーザーネーム
UN = ""

#認証
client = tweepy.Client(bearer_token=BT, consumer_key=CK, consumer_secret=CS, access_token=AT, access_token_secret=ATS)

#自分のID検索
search = str(client.get_user(username=UN))
UID = re.findall("(?<=User id=)\w+", search)[0]

#ツイートとツイートID検索
tweets = str(client.get_users_tweets(id=UID))
TID = re.findall("(?<=Tweet id=)\w+", tweets)[0]
tweet = re.findall("(?<=text=)\w+", tweets)[0]

#ツイート検索&実行
if tweet == "ライトつけて" :
    client.create_tweet(in_reply_to_tweet_id=TID, text="つけました！")
    requests.post(url, headers=h, json=j)
    print("実行しました！")
elif tweet == "ライトけして" :
    client.create_tweet(in_reply_to_tweet_id=TID, text="けしました！")
    requests.post(url, headers=h, json=j)
    print("実行しました！")
else:
    print("見つかりませんでした")