import requests
from requests.structures import CaseInsensitiveDict
import time
import datetime
# import random

# Prepare words list
start = time.time()
words = []

# Parse the txt file,
# and store the words in a list
with open('dictionnaries/tiny_list.txt') as f:
  line = f.readline()
  while line:
    line = f.readline()
    words.append(line.rstrip('\n'))

# Cemantix API URL
url = 'https://cemantix.herokuapp.com/score'

# Headers definitions
headers = CaseInsensitiveDict()
headers['Content-Type'] = 'application/x-www-form-urlencoded'
headers['Host'] = 'cemantix.herokuapp.com'
headers['Origin'] = 'https://cemantix.herokuapp.com'
headers['referrer'] = 'https://cemantix.herokuapp.com/'
headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'

# Iterating through the txt list but in reverse order
def main():
  # random.shuffle(words)
  for word in reversed(list(words)):
    data = f'word={word}'.encode('utf-8')

    resp = requests.post(url, headers=headers, data=data)
      
    score = resp.json()
    
    if 'score' in score:
      print(f"{word} ➡️ {score['score']}")
      if score['score'] == 1:
        end = time.time()
        print(f'Result: {word} 🥳 in {str(datetime.timedelta(seconds = end - start))}')
        break

main()
