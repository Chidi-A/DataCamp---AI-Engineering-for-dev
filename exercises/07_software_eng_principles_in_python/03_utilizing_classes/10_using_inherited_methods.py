# Import needed package
import text_analyzer

# Create instance of Tweets
my_tweets = text_analyzer.Tweets(datacamp_tweets)

# Plot the most used hashtags in the tweets
my_tweets.plot_counts('hashtag_counts')

# Plot the most used hashtags in the retweets
my_tweets.plot_counts('retweets.hashtag_counts')

help(my_tweets.plot_counts)