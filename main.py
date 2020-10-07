import requests
from pprint import pprint
import argparse

# Initialize the parser
parser = argparse.ArgumentParser(description='Github')
# Required positional argument (username)
parser.add_argument('-u', '--user', dest='type', required=True,
                    help='Github username must be passed through the argument')
args = parser.parse_args()
username = args.type
# url to request
url = f"https://api.github.com/users/{username}"
# make the request and return the json
user_data = requests.get(url).json()
# pretty print JSON data
pprint(user_data)
pprint(user_data['company'])