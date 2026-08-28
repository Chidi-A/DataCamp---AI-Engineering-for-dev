from collections import Counter
from text_analyzer import SocialMedia

# Create an instance of SocialMedia for testing
test_post = 'learning #python & #rstats is awesome! thanks @datacamp!'
sm_post = SocialMedia(test_post)

# Test hashtag counts are created properly
def ____social_media_hashtags():
    expected_hashtag_counts = Counter({'#python': 1, '#rstats': 1})
    ____ sm_post.hashtag_counts == expected_hashtag_counts