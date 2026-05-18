import re

def parse_deck_list(texto):
    cartas = []
    linhas = texto.splitlines()
    for linha in linhas:
        linha = linha.strip()
        if linha == "":
            continue
        match = re.match(
            r"(\d+)\s+(.+?)\s+\(([A-Z0-9]+)\)\s+(\d+)",
            linha
        )
        if match:
            quantidade = int(match.group(1))
            nome = match.group(2)
            set_code = match.group(3)
            collector_number = match.group(4)
            cartas.append({
                "qty": quantidade,
                "name": nome,
                "set": set_code.lower(),
                "collector_number": collector_number
            })
    return cartas