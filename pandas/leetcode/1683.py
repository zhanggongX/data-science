import pandas as pd


def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    df = tweets[tweets['content'].str.len() > 15]
    # df = df[['tweet_id']]
    return df[['tweet_id']]


if __name__ == '__main__':
    data = [[1, 'Vote for Biden'], [2, 'Let us make America great again!']]
    Tweets = pd.DataFrame(data, columns=['tweet_id', 'content']).astype({'tweet_id': 'Int64', 'content': 'object'})

    res = invalid_tweets(Tweets)
    print(res)
