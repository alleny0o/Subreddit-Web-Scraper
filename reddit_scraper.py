import praw
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Access the variables
client_id = os.getenv('CLIENT_ID')
client_secret = os.getenv('SECRET_KEY')
user_agent = os.getenv('user_agent')

# Initialize Reddit instance
reddit = praw.Reddit(
    client_id=client_id,
    client_secret=client_secret,
    user_agent=user_agent
)

# Get subreddit name from user input
subreddit_name = input("Enter the name of the subreddit you want to explore: ")
subreddit = reddit.subreddit(subreddit_name)
top_posts = subreddit.hot(limit=10)

for post in top_posts:
    print(f"Title: {post.title}")
    print(f"Body: {post.selftext}\n")
