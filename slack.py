import requests
import os


def post_to_slack(file_name, msg):
    try:
        headers = {
            'Authorization': 'Bearer xoxb-XXXXXXXXXXXXX-XXXXXXXXXXXXX-XXXXXXXXXXXXXXXXXXXXXXXX'}

        files = {
            'file': open(file_name, 'rb'),
            'initial_comment': (None, msg),
            'channels': (None, '<channel names separated with commas>')}

        res = requests.post(
            'https://slack.com/api/files.upload', headers=headers, files=files)
        print(res)
    except Exception as e:
        print(e)
