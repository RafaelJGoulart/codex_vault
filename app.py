import webview
import json


class Api:
    def get_decks(self):
        with open("decks.json", "r", encoding="utf-8") as f:
            return json.load(f)


if __name__ == "__main__":
    api = Api()
    
    window = webview.create_window(
        "CodexVault",
        "frontend/pages/index.html",
        js_api=api,
        #frameless=True
    )
    
    webview.start()
