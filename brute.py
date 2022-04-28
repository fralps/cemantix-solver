import os
import requests
from requests.structures import CaseInsensitiveDict
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv

load_dotenv()

SENDER_ADDRESS = os.getenv('SENDER_ADDRESS')
SENDER_PASSWORD = os.getenv('SENDER_PASSWORD')

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

# Iterating through the txt list
def main():
  for word in words:
    data = f'word={word}'

    resp = requests.post(url, headers=headers, data=data)
      
    score = resp.json()
    
    if 'score' in score:
      print(f"{word} ➡️ {score['score']}")
      if score['score'] > 0.1:
        print(f'Result: {word} 🥳')
        # send_result(word)
        break


def send_result(result):
  port_number = 1234
  msg = MIMEMultipart()
  msg['From'] = SENDER_ADDRESS
  msg['To'] = 'cemantixsolver@yopmail.com'
  msg['Subject'] = 'Result of the day'
  message = f'The result is: {result} 🎉'
  msg.attach(MIMEText(message))
  mailserver = smtplib.SMTP('localhost', port_number)
  mailserver.login(SENDER_ADDRESS, SENDER_PASSWORD)
  mailserver.sendmail(SENDER_ADDRESS, 'cemantixsolver@yopmail.com', msg.as_string())
  mailserver.quit()

  print('Email Sent')

main()
