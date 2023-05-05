import praw
import pandas as pd
from datetime import date


def get_reddit_posts(file_name):
    try:
        reddit = praw.Reddit(client_id='<client_id>',
                             client_secret='<client_secret>',
                             user_agent='<user_agent>',
                             username='<username>',
                             password='<password>'
                             )

        with open('search_terms/reddit_groups.txt') as f:
            groups = [line.rstrip('\n')
                      for line in f if not line.startswith('#')]

        data = []
        for group in groups:
            for submission in reddit.subreddit(group).top(time_filter="day"):
                try:
                    posts = {}
                    posts['group'] = group
                    posts['title'] = submission.title.encode('ascii', 'ignore')
                    posts['url'] = submission.url.encode('ascii', 'ignore')
                    posts['text'] = submission.selftext[:120].encode(
                        'ascii', 'ignore')

                    data.append(posts)
                except:
                    continue

        df = pd.DataFrame(data)
        df.to_csv(file_name)

    except Exception as e:
        print(e)
        return
