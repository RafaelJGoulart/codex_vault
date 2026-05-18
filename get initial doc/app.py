import requests
import json

# Nome da carta
nome_carta = "Counterspell"

# URL da API
url = f"https://api.scryfall.com/cards/named?exact={nome_carta}"

# Faz a requisição
response = requests.get(url)

# Verifica se deu certo
if response.status_code == 200:

    # Converte para JSON
    carta = response.json()

    # Mostra algumas informações
    print("Nome:", carta["name"])
    print("Mana Cost:", carta["mana_cost"])
    print("Tipo:", carta["type_line"])
    print("Poder:", carta.get("power", "N/A"))
    print("Resistência:", carta.get("toughness", "N/A"))

    print("\nTexto:")
    print(carta["oracle_text"])

    print("\nImagem:")
    print(carta["image_uris"]["normal"])

    # Salva o JSON completo em arquivo
    with open(nome_carta, "w", encoding="utf-8") as arquivo:
        json.dump(carta, arquivo, ensure_ascii=False, indent=4)

    print(f"\nJSON salvo como {nome_carta}")

else:
    print("Erro ao buscar carta.")
    print("Código:", response.status_code)