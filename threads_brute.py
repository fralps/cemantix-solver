# Modules definitions
import requests
import threading
from requests.structures import CaseInsensitiveDict
import numpy as np
import time
import datetime

# Prepare timer, words list and threads exit event
start = time.time()
words = []
exit_event = threading.Event()

# Parse the txt file,
# and store the words in a list
with open('dictionnaries/tiny_list.txt') as file:
  line = file.readline()
  while line:
    line = file.readline()
    words.append(line.rstrip('\n'))

# Take words from the list and randomize them with shuffle
random_list = np.array(words)
np.random.shuffle(random_list)

# Cemantix API URL
url = 'https://cemantix.herokuapp.com/score'

# Headers definitions
headers = CaseInsensitiveDict()
headers['Content-Type'] = 'application/x-www-form-urlencoded'
headers['Host'] = 'cemantix.herokuapp.com'
headers['Origin'] = 'https://cemantix.herokuapp.com'
headers['referrer'] = 'https://cemantix.herokuapp.com/'
headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'

# Solve and find word of the day
def solve(list, reversed):
  if reversed:
    list = list[::-1]

  for word in list:
    data = f'word={word}'.encode('utf-8')
    resp = requests.post(url, headers=headers, data=data)
    score = resp.json()
    
    if 'score' in score:
      print(f"\033[0;37m{word} ➡️ {score['score']}")
      if score['score'] == 1:
        end = time.time()
        print(f'\033[1;32mResult: {word} in {str(datetime.timedelta(seconds = end - start))} 🥳')
        exit_event.set()
        break
      
      # Stopping remaining threads if the word is found
      if exit_event.is_set():
        break

# Run script and threads definitions
def main():
  threading.Thread(target = solve, args = [words, False]).start()
  threading.Thread(target = solve, args = [words, True]).start()
  threading.Thread(target = solve, args = [random_list, False]).start()
  threading.Thread(target = solve, args = [random_list, True]).start()
  
main()
