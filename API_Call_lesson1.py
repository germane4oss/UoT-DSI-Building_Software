import requests
import json
from pprint import pprint

# get secret from Colab
from google.colab import userdata
token = userdata.get('germane4oss')

# initialize request parameters
url = 'https://api.github.com/search/repositories?q=stars:>1&sort=stars&order=desc'
headers = {'Authorization': 'Bearer ' + token}

# send request to GitHub
r = requests.get(url, headers=headers)

#Convert the response to json

r_json = json.loads(r.text)

# Load json into a dictionary

items = r_json['items']
# Define repo_name and repo_starts arrays for plotting

repo_name=[]
repo_stars=[]

# Iterate the received data to populate repo_name and repo_stars

for item in items:
  repo_name.append(item['name'])
  repo_stars.append(item['stargazers_count'])

# import matplotlib

import matplotlib.pyplot as plt

# plot the data

plt.barh(repo_name, repo_stars)
