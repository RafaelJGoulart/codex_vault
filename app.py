import webview
import json
import os

from deck_parser import parse_deck_list

DECK_PATH = "data/decks"
os.makedirs(DECK_PATH, exist_ok=True)

class Api:
    def salvarDeck(self, deck):

        cartas = parse_deck_list(deck["list"])

        deck_json = {
            "name": deck["name"],
            "commander": deck["commander"],
            "cards": cartas
        }

        file_name = deck["name"].lower().replace(" ", "_") + ".json"

        path = os.path.join(DECK_PATH, file_name)

        with open(path, "w", encoding="utf8") as f:
            json.dump(deck_json, f, indent=4)

        return True


if __name__ == "__main__":
    api = Api()
    
    window = webview.create_window(
        "CodexVault",
        "frontend/pages/index.html",
        js_api=api,
        width=900,
        height=600,
        resizable=True,   # permite redimensionar
        min_size=(500, 400) # tamanho mínimo
          
        #frameless=True
        
    )
    
    webview.start()
