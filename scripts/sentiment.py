from pymongo import MongoClient
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from dotenv import load_dotenv
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
env_path = os.path.join(script_dir, '..', '.env.local')
load_success = load_dotenv(env_path)

# MongoDB setup
client = MongoClient(os.getenv('MONGODB_URI'))
db = client['retro-tracker']
posts_collection = db['posts']

# VADER setup
analyzer = SentimentIntensityAnalyzer()

def analyze_sentiment():
    posts = posts_collection.find({'sentiment': {'$exists': False}})
    for post in posts:
        scores = analyzer.polarity_scores(post['text'])
        sentiment = 'positive' if scores['compound'] > 0.05 else 'negative' if scores['compound'] < -0.05 else 'neutral'
        posts_collection.update_one(
            {'_id': post['_id']},
            {'$set': {'sentiment': sentiment, 'score': scores['compound']}}
        )

if __name__ == '__main__':
    analyze_sentiment()