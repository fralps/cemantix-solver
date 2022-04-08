import requests
import json
from requests.structures import CaseInsensitiveDict

# Opening JSON file
file = open('index.json')
 
# Returns JSON object as a dictionary
words = json.load(file)

# Cemantix API URL
url = 'https://cemantix.herokuapp.com/score'

# Headers definitions
headers = CaseInsensitiveDict()
headers['Content-Type'] = 'application/x-www-form-urlencoded'
 
# Iterating through the json list
for word in words:
  data = f'word={word}'

  resp = requests.post(url, headers=headers, data=data)
    
  score = resp.json()
  
  if 'score' in score:
    if score['score'] < 0.2652:
      print(f"{word} : {score['score']} 🥶")
    elif score['score'] < 0.4527:
      print(f"{word} : {score['score']} 😎")
    elif score['score'] < 0.6231:
      print(f"{word} : {score['score']} 🥵")
    elif score['score'] < 0.7679:
      print(f"{word} : {score['score']} 🔥")
    elif score['score'] < 1:
      print(f"{word} : {score['score']} 😱")
    elif score['score'] == 1:
      print(f'Result: {word} 🥳')
      break
    
 
# Closing file
file.close()
