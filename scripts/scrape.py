import praw
from pymongo import MongoClient
from dotenv import load_dotenv
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
env_path = os.path.join(script_dir, '..', '.env.local')
load_success = load_dotenv(env_path)

# Reddit API setup
reddit = praw.Reddit(
    client_id=os.getenv('REDDIT_CLIENT_ID'),
    client_secret=os.getenv('REDDIT_CLIENT_SECRET'),
    user_agent=os.getenv('REDDIT_USER_AGENT')
)

# MongoDB setup
client = MongoClient(os.getenv('MONGODB_URI'))
db = client['retro-tracker']
posts_collection = db['posts']

def scrape_retrogaming():
    subreddit = reddit.subreddit('retrogaming')
    for post in subreddit.hot(limit=10):  # Scrape 10 posts
        posts_collection.insert_one({
            'game': post.title.lower(),  # Simplified game detection
            'text': post.selftext or post.title,
            'timestamp': post.created_utc
        })

if __name__ == '__main__':
    scrape_retrogaming()