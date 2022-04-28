import requests
from requests.structures import CaseInsensitiveDict

# Prepare words list
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

# Iterating through the txt list but in reverse order
def main():
  for word in reversed(list(words)):
    data = f'word={word}'

    resp = requests.post(url, headers=headers, data=data)
      
    score = resp.json()
    
    if 'score' in score:
      print(f"{word} ➡️ {score['score']}")
      if score['score'] > 0.10:
        print(f'Result: {word} 🥳')
        break

main()
