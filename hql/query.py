"""Query and set up the environment"""

import requests


def main(url):
    print('File Querying: ' + url)
    response = requests.get(url)
    print('Status: %d' % response.status_code)
    print(response.text)
