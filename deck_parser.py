import re

def parse_deck_list(texto):

    cartas = []

    linhas = texto.splitlines()

    for linha in linhas:

        linha = linha.strip()

        if linha == "":
            continue

        match = re.match(r"(\d+)\s+(.+)", linha)

        if match:

            quantidade = int(match.group(1))
            nome = match.group(2)

            cartas.append({
                "qty": quantidade,
                "name": nome
            })

    return cartas