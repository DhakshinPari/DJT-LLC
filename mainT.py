import tweepy
import time

api_key = 'cKkCs40uSlEIGVtE8B6JgXCKW'
api_key_secret = '2n977XlEsnb5NVRPRX1qoojzrxIqeBLyzma7GyYzxmNsxI2hrK'
access_token = '1521275495618334720-7fDhZTfhhv5eYCarUFtnQIh4uzr2ar'
access_token_secret = '5caHqGBzUtKFQP2FrQ6qyau6VM31ls3S8JR5Jdbf7tXUg'

# auth = tweepy.OAuthHandler(api_key, api_key_secret)
# auth.set_access_token(access_token, access_token_secret)


authenticator = tweepy.OAuthHandler(api_key, api_key_secret)
authenticator.set_access_token(access_token, access_token_secret)

api = tweepy.API(authenticator, wait_on_rate_limit=True)


# automated tweet
# checks to see last stored tweet
def read_last_seen(FILE_NAME):
    file_read = open(FILE_NAME, 'r')
    last_seen_id = int(file_read.read().strip())
    file_read.close()
    return last_seen_id


def store_last_seen(FILE_NAME, last_seen_id):
    file_write = open(FILE_NAME, 'w')
    file_write.write(str(last_seen_id))
    file_write.close()
    return


def reply():
    tweets = api.media_upload('elon1.jpg')
    tweets = api.media_upload('tslalg.jpg')
    for _ in tweets:
        if '#ISPDJT1' in tweet.full_text.lower():
            print(str(tweet.id) + 'transaction_type', 'company', 'insider_relationship', 'shares_traded',
                  'average_price',
                  'Buy/Sell: Sell')
            return api.update_status


while True:
    reply()
    time.sleep(15)

# auto like tweet
user = api.get_user("ISPDJT1")
tweets_user = api.user_timeline(user_id=user.id)

for tweet in tweets_user:
    if not tweet.favorited:
        api.create_favorite(tweet.id)
