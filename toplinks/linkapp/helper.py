from urllib.parse import urlparse
from datetime import datetime


def get_domain(url):
    '''Take out Domain from the URLs'''
    p_url = urlparse(url)
    result = '{uri.netloc}'.format(uri=p_url)
    return result


def past_7_days(tweets):
    '''Filter out Past 7 days Tweets'''

    all_tweet_data = []
    for tweet in tweets:
        urls = tweet.entities.get('urls')
        days = (datetime.now() - tweet.created_at).days
        if urls and days <= 7:
            tweet_, domain = {}, {}
            tweet_['tweet_id'] = tweet.id_str
            domain['tweet_id'] = tweet.id_str
            tweet_['text'] = tweet.full_text
            tweet_['url'] = urls[0].get('expanded_url')
            tweet_['user_id'] = tweet.user.id_str
            tweet_['user_name'] = tweet.user.name
            domain['domain_name'] = get_domain(tweet_['url'])
            all_tweet_data.append((tweet_, domain))
    return all_tweet_data
