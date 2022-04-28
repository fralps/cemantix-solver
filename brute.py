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
      if score['score'] > 0.10:
        print(f'Result: {word} 🥳')
        send_result(word)
        break


def send_result(result):
  # The email addresses and password
  gmail_port = 587

  receiver_address = 'cemantixsolver@yopmail.com'
  mail_content = f'Result of the day.... {result} 🎉'

  # Setup the MIME
  message = MIMEMultipart()
  message['From'] = SENDER_ADDRESS
  message['To'] = SENDER_PASSWORD
  message['Subject'] = 'Cemantix results'

  # The body and the attachments for the mail
  message.attach(MIMEText(mail_content, 'plain'))

  # Create SMTP session for sending the mail
  session = smtplib.SMTP('smtp.gmail.com', gmail_port)
  session.starttls() # enable security
  session.login(SENDER_ADDRESS, SENDER_PASSWORD)
  text = message.as_string()
  session.sendmail(SENDER_ADDRESS, receiver_address, text)
  session.quit()

  print('Email Sent')

main()
