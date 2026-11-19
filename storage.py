import json
from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parent
DATA_FILE = PROJECT_DIR / "links.json"

def save_links(links):
    with open(DATA_FILE,"w",encoding="utf-8") as file:
        json.dump(links,file,indent=4)
          


def load_links():
    try:
        with open(DATA_FILE,"r",encoding="utf-8") as file:
                saved_links = json.load(file)
                return saved_links
    except FileNotFoundError:
         return []
    except json.JSONDecodeError:
        return []



      



