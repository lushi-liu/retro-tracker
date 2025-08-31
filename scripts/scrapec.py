import praw
from pymongo import MongoClient
import prawcore
import os

## print(os.environ)
print("REDDIT_CLIENT_ID:", os.environ.get('REDDIT_CLIENT_ID'))
print("REDDIT_CLIENT_ID:", os.getenv('REDDIT_CLIENT_ID'))
print("REDDIT_CLIENT_SECRET:", os.getenv('REDDIT_CLIENT_SECRET'))
print("REDDIT_USER_AGENT:", os.getenv('REDDIT_USER_AGENT'))
print("MONGODB_URI:", os.getenv('MONGODB_URI'))

# Hardcoded credentials for debugging
try:
    reddit = praw.Reddit(
        client_id='SY71gyeOvQXXZjeCxzco_g',  # Replace with new 14-character client_id
        client_secret='UPkCfc_nFjsNmbrO2J62avFORx3dOw',  # Replace with new secret key
        user_agent='retro-tracker'
    )
    # Test API connection
    reddit.user.me()  # Should return None for script apps but validates auth
    print("Reddit API initialized successfully")
except prawcore.exceptions.ResponseException as e:
    print(f"Reddit API error: {str(e)}")
    raise
except Exception as e:
    print(f"Unexpected Reddit error: {str(e)}")
    raise

# MongoDB setup
try:
    client = MongoClient('mongodb+srv://lushiliu1_db_user:swds3vZ6gSc2H3dn@cluster0.yxtupxb.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')  # Replace with your MongoDB URI
    db = client['retro-sentiment']
    posts_collection = db['posts']
    print("MongoDB connected successfully")
except Exception as e:
    print("MongoDB error:", str(e))
    raise

def scrape_retrogaming():
    try:
        subreddit = reddit.subreddit('retrogaming')
        for post in subreddit.hot(limit=10):  # Scrape 10 posts
            posts_collection.insert_one({
                'game': post.title.lower(),
                'text': post.selftext or post.title,
                'timestamp': post.created_utc
            })
            print(f"Inserted post: {post.title}")
    except prawcore.exceptions.ResponseException as e:
        print(f"Scraping error: {str(e)}")
        raise
    except Exception as e:
        print(f"Unexpected scraping error: {str(e)}")
        raise

if __name__ == '__main__':
    scrape_retrogaming()