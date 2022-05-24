# Modules definitions
import requests
from requests.structures import CaseInsensitiveDict

# Prepare words list
words = []

# Parse the txt file,
# and store the words in a list
with open('dictionnaries/english3.txt') as f:
  line = f.readline()
  while line:
    line = f.readline()
    words.append(line.rstrip('\n'))

# Cemantle API URL
url = 'https://cemantle.herokuapp.com/score'

# Headers definitions
headers = CaseInsensitiveDict()
headers['Content-Type'] = 'application/x-www-form-urlencoded'
headers['Host'] = 'cemantle.herokuapp.com'
headers['Origin'] = 'https://cemantle.herokuapp.com'
headers['referrer'] = 'https://cemantle.herokuapp.com/'
headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'

# Iterating through the txt list
def main():
  for word in words[words.index('validly'):]:
    data = f'word={word}'.encode('utf-8')
    resp = requests.post(url, headers=headers, data=data)
    score = resp.json()

    if 'score' in score:
      print('SCORE:', score['score'])
      clean(word)
    else:
      print(f"{word} - {score}")

def clean(word):
  with open('dictionnaries/cleaned.txt', 'a') as f:
    f.write(f"{word}\n")

main()