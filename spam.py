import requests
from requests.structures import CaseInsensitiveDict
import time

word = 'chasse'

# Cemantix API URL
url = 'https://cemantix.herokuapp.com/score'

# Headers definitions
headers = CaseInsensitiveDict()
headers['Content-Type'] = 'application/x-www-form-urlencoded'
headers['Host'] = 'cemantix.herokuapp.com'
headers['Origin'] = 'https://cemantix.herokuapp.com'
headers['referrer'] = 'https://cemantix.herokuapp.com/'
headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'  

def main():  
  for i in range(2000):
    data = f'word={word}'.encode('utf-8')
    resp = requests.post(url, headers=headers, data=data)  
    score = resp.json()
  
    if 'score' in score:
      print(f"{i} ➡️ {score['score']}")
    
    time.sleep(1)

main()
