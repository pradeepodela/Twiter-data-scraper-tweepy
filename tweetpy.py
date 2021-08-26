
import tweepy
import pandas as pd

API_KEY = '2hSBVPG4ESWYNCEKo5GngSn6J'
API_SECRATE_KEY = 'jBHcUaJqTwkkw9iiXYo3CfePzPnb881jC5ikW7ZjnNNW3ztESW'
BARRER_TOKEN = 'AAAAAAAAAAAAAAAAAAAAADb1SwEAAAAA4VzjrjotQpsJ9FZatrait8ln0Gc%3DQLoheq5suKo04mofhDKSkBdS1gKhy2Kyv51WMxtxb9jFHo1YKs'
ACCESS_TOKEN = '1360835306098843650-RqDlX5OA3bBfzpznW3o7fNbwH5jp9S'
ACESS_TOKEN_SECRATE = 'J2oedvRdZeG2Fem5LGiE0HfQku6Hagw2ZYvJEQZwyea6q'
QUARY = 'elon musk'


# Comprobamos la conexión.
auth = tweepy.OAuthHandler(consumer_key=API_KEY,consumer_secret=API_SECRATE_KEY)
auth.set_access_token(key=ACCESS_TOKEN , secret=ACESS_TOKEN_SECRATE)

api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")
test = []
tweets = []
username = []
screen_name = []
date = []
hashtags = []
tweet_url = []
mentions = []
verified = []
dedescription = []
friends_count = []
retweet = []
followers_count = []
retweet_count= []
likes = []
results = {}
for tweet in api.search(q=QUARY, lang="en", rpp=5000, count=1000 ):
    tmp = tweet.entities['hashtags']
    test.append(tweet)
    tweets.append(tweet.text)
    username.append(tweet.user.name)
    screen_name.append('@'+tweet.user.screen_name)
    date.append(tweet.created_at)
    hashtags.append(tweet.entities['hashtags'])
    mentions.append(tweet.entities['user_mentions'])
    #retweet.append(tweet.retweet._json.text)
    retweet_count.append(tweet.retweet_count)
    followers_count.append(tweet.user.followers_count)
    verified.append(tweet.user.verified)
    dedescription.append(tweet.user.description)
    friends_count.append(tweet.user.friends_count)
   # print(tweet.user['followers_count'])
    #print(' ')
    #tweet_url.append(tweet.urls['url'])
    
# Creamos un dataframe con la busqueda realizada.
results = pd.DataFrame({'username':username, 'screen_name':screen_name, 'date':date, 'tweet':tweets, 'hashtags': hashtags  , 'mention':mentions , 'retweet_count':retweet_count , 'followers_count':followers_count ,'verified':verified,'following':friends_count, 'dedescription':dedescription})

results.to_csv('tweets.csv')