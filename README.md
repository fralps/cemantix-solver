# cemantix-solver/cemantle-solver 🐍

*Python scripts to find Cemantix and Cemantle daily word by brute forcing apps api.* 

ℹ️ *Disclaimer: I did this project to learn Python basics, so feel free to give me your feedbacks*

- [Cemantix results Notion database](https://bead-cylinder-699.notion.site/fe486d80a5994c02af48af8dbe3d4f96?v=59ad4e14485d477da756a04999190730)
- [Cemantle results Notion database](https://bead-cylinder-699.notion.site/6440b74a3e6f4d9c9819e0e40eb6613d?v=4db027d34f11496ca09786f996703914)

### Requirements

- Python version: `>= 3`
- Pip version: `23.0.1`
- Notion account

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

**or**

If you do not have a Notion database, you can simply comment the `send_to_notion()` function call in the scripts and see the result directly in your terminal 🤓


3. Finally, you can run scripts with the following commands lines:
- Cemantix --> `python3 cemantix-solver.py`
- Cemantle --> `python3 cemantle-solver.py`

### Dictionaries

You can find all words in the `./dictionnaries` folder for French and English locales. There are two dictionnaries available for each locale: one fat list with many words and another one with less word.

### Github Actions

We use Github Actions to run scripts to find word everyday and fill Notion databases.

Workflows can be found in `.github/workflows` folder.

### Others

`cleaner.py` was used to clean initial dictionnaries for words that were not found by cemantix/cemantle API. You can use `cleaner.py` if you want to add another dictionnary.

### Contribute
Please feel free to open PR with your awesome ideas 💡

### Thanks 🙏🏼

You can go to the awesome websites of [Cemantix](https://cemantix.certitudes.org/) and [Cemantle](https://cemantle.certitudes.org/) made by David Turner and maintained by [Julie](https://twitter.com/cemantle) and [enigmatix](https://twitter.com/enigmathix).
