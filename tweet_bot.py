import tweepy
import csv
import random

# ─── Credentials ─────────────────────────────────────────────────────
API_KEY = "dUzA1M0JI6Cp2CwKuHXUlVXmU"
API_SECRET = "tYZ6DjEcXnDawBJolVHh4eP5qvN44v2TjyYZKs6MmqdpCd90xt"
ACCESS_TOKEN = "1501376964111732738-6DKh8ZdUcCtxplX8J2eVUZnCJoV0BS"
ACCESS_SECRET = "1jCXh0jiUsaD94smW5lvYlAW1CbNHVeSgLhagFADIrPfc"
BEARER_TOKEN = "AAAAAAAAAAAAAAAAAAAAAKCL2gEAAAAA7yIqjEZuDje%2Fh7RAqOQv25D8p3w%3DtISsqJkVn7JzdKtt2fBahX1sFaaVkUe4TfQ6dmJhzCGkZJyaqC"

# ─── Load a random quote from quotes.csv ─────────────────────────────
def get_random_quote():
    with open("quotes.csv", "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        quotes = [row for row in reader]

    chosen = random.choice(quotes)
    quote_text = chosen["quote"].strip()
    author = chosen["author"].strip()

    # Optional: truncate if it's too long
    full_tweet = quote_text
    if len(full_tweet) > 280:
        full_tweet = full_tweet[:277] + "..."

    return full_tweet

# ─── Initialize Tweepy client ────────────────────────────────────────
client = tweepy.Client(
    bearer_token=BEARER_TOKEN,
    consumer_key=API_KEY,
    consumer_secret=API_SECRET,
    access_token=ACCESS_TOKEN,
    access_token_secret=ACCESS_SECRET
)

# ─── Post the quote tweet ────────────────────────────────────────────
if __name__ == "__main__":
    tweet_text = get_random_quote()
    try:
        response = client.create_tweet(text=tweet_text)
        print("✅ Tweet posted:", response.data["id"])
    except Exception as e:
        print("❌ Failed to post tweet:", e)
