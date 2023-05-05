from datetime import date
from slack import post_to_slack
from reddit import get_reddit_posts
import os


def remove_file(file_name):
    if os.path.exists(file_name):
        os.remove(file_name)


def main():
    today = date.today()
    file_name = 'reddit_' + str(today) + '.csv'
    get_reddit_posts(file_name)
    post_to_slack(file_name, 'Reddit searches for today!')
    remove_file(file_name)


if __name__ == "__main__":
    main()
