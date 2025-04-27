import os
import dotenv
import tweepy

dotenv.load_dotenv()
donsumer_key = os.getenv("CONSUMER_KEY")
consumer_secret = os.getenv("CONSUMER_SECRET")
bearer_token = os.getenv("BEARER_TOKEN")
access_token = os.getenv("ACCESS_TOKEN")
access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")

api_auth = tweepy.OAuth2BearerHandler(bearer_token)

api = tweepy.Client(
    consumer_key=consumer_key,
    consumer_secret=consumer_secret,
    bearer_token=bearer_token,
    access_token=access_token,
    access_token_secret=access_token_secret,
)

tweet = "これはAI Tuber本のテストポストです"

try:
    api.create_tweet(text=tweet)
    print("ポストの投稿に成功しました！")
except tweepy.TweepError as e:
    print(f"エラーが発生しました: {e}")
