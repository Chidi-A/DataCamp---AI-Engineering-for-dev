# load the Counter function into our environment
from collections import Counter

# View the documentation for Counter.most_common
help(Counter.most_common)


# use Counter to find the top 5 most common words
top_5_words = Counter("data science is a field that uses scientific methods, processes, algorithms and systems to extract knowledge and insights from data".split()).most_common(5)

# display the top 5 most common words
print(top_5_words)
