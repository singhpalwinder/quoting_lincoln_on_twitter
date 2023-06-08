import tweepy
import random
import credentials


#0auth1 authentication
client = tweepy.Client(
    consumer_key=credentials.API_KEY,
    consumer_secret=credentials.API_KEY_SECRET,
    access_token=credentials.ACCESS_TOKEN,
    access_token_secret=credentials.ACCESS_TOKEN_SECRET
)
 

 
if(client):
    print('Successful connection')
else:
    print('Failed connection')


quote = ""

while True:
    try:
        with open("quotes.txt", 'r') as f:
            lines = [quote.strip() for quote in f if quote.strip() and quote.strip()[-1] == '.']
            quote = random.choice(lines)
            break
    except:
        print("Error opening file")

tweet = (quote + str('\n-Abraham Lincoln'))

client.create_tweet(text=tweet)