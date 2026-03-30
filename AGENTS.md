# Agents

## Project Overview

Python scripts to brute-force the [Cemantix](https://cemantix.certitudes.org/) and [Cemantle](https://cemantle.certitudes.org/) daily word puzzles by querying their APIs.

## Python Version

- **Required**: >= 3.11 (Python 3.14.2 with pyenv in use)
- **Installation via pyenv**: `pyenv install 3.11` or use system Homebrew Python

## Setup

```bash
# Create and activate virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install requests python-dotenv numpy
```

## Running Scripts

```bash
# Activate environment and run
source .venv/bin/activate
python3 cemantix_solver.py    # French puzzle
python3 cemantle_solver.py     # English puzzle
```

## Environment Variables

Create a `.env` file at the project root:

```env
# Notion integration (optional - scripts work without these)
CEMANTIX_DATABASE_ID=your-cemantix-database-id
CEMANTIX_NOTION_TOKEN=your-cemantix-notion-token
CEMANTLE_DATABASE_ID=your-cemantle-database-id
CEMANTLE_NOTION_TOKEN=your-cemantle-notion-token
```

## Dictionaries

| File | Language | Path |
|------|----------|------|
| fr_tiny_list.txt | French | `dictionnaries/fr/` |
| en_tiny_list.txt | English | `dictionnaries/en/` |

## Architecture

- **cemantix_solver.py**: French word solver (28 threads)
- **cemantle_solver.py**: English word solver (28 threads)
- **cleaner.py**: Utility to clean dictionary files
- **.github/workflows/**: GitHub Actions for daily automated runs

## Testing

```bash
python3 -m py_compile cemantix_solver.py
python3 -m py_compile cemantle_solver.py
```

## Common Issues

- **"Access denied"**: IP temporarily blocked by Cemantix - wait 15-30 minutes
- **ModuleNotFoundError**: Wrong Python environment - ensure `.venv` is activated
- **PEP 668 externally-managed-environment**: Use virtual environment (`python3 -m venv .venv`)
