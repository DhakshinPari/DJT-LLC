import tweepy

api_key = 'cKkCs40uSlEIGVtE8B6JgXCKW'
api_key_secret = '2n977XlEsnb5NVRPRX1qoojzrxIqeBLyzma7GyYzxmNsxI2hrK'
access_token = '1521275495618334720-7fDhZTfhhv5eYCarUFtnQIh4uzr2ar'
access_token_secret = '5caHqGBzUtKFQP2FrQ6qyau6VM31ls3S8JR5Jdbf7tXUg'

#auth = tweepy.OAuthHandler(api_key, api_key_secret)
#auth.set_access_token(access_token, access_token_secret)


authenticator = tweepy.OAuthHandler(api_key, api_key_secret)
authenticator.set_access_token(access_token, access_token_secret)


api = tweepy.API(authenticator, wait_on_rate_limit=True)




