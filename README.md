# cemantix-solver/cemantle-solver

*Python scripts to find Cemantix and Cemantle daily word by brute forcing apps api.*

ℹ️ *Disclaimer: I did this project to learn Python basics, so feel free to give me your feebacks*

### Requirements

- Python version: `>= 3`
- Pip version: `22.3`

### Getting started

1. You will need the following packages in order to make scripts work:
- `requests` --> `pip3 install requests`
- `python-dotenv` --> `pip3 install python-dotenv`
- `numpy` --> `pip3 install numpy`
- `datetime` --> `pip3 install datetime`

2. Then, you can add a `.env` file at the root of your folder with those env variables:
```
CEMANTLE_DATABASE_ID = your-cemantle-database-id
CEMANTIX_DATABASE_ID = your-cemantix-database-id
CEMANTLE_NOTION_TOKEN = your-cemantle-notion-token
CEMANTIX_NOTION_TOKEN = your-cemantIX-notion-token
```

3. Finally, you can run scripts with the following commands lines:
- Cemantix --> `python3 cemantix-solver.py`
- Cemantle --> `python3 cemantle-solver.py`

### Dictionaries

You can find all words in the `./dictionnaries` folder for French and English locales. There are two dictionnaries available for each locale: one fat list with many words and another one with less word.

### Github Actions
We use Github Actions to run scripts to find word everyday and fill Notion database

Workflows can be found in `.github/workflows` folder.

### Contribute
Please feel free to open PR with your awesome ideas 💡
