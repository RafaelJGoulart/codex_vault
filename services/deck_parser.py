import re


def parse_deck_list(texto):
    cartas = []
    linhas = texto.splitlines()
    for linha in linhas:
        linha = linha.strip()
        # ignora linhas vazias
        if linha == "":
            continue
        # ignora comentários
        if linha.startswith("#"):
            continue
        # ignora sideboard por enquanto
        if linha.upper().startswith("SB:"):
            continue
        """
        FORMATO COMPLETO

        Exemplos:
        1 Arcane Signet (C20) 237
        1 Frontier Bivouac (PLST) C17-251
        2 Sol Ring (CLB) 304
        """

        full_match = re.match(
            r"(\d+)x?\s+(.+?)\s+\(([A-Z0-9]+)\)\s+([A-Z0-9\-\*]+)",
            linha,
            re.IGNORECASE
        )
        if full_match:
            quantidade = int(full_match.group(1))
            nome = full_match.group(2).strip()
            set_code = full_match.group(3).lower()
            collector_number = full_match.group(4)

            cartas.append({
                "qty": quantidade,
                "name": nome,
                "set": set_code,
                "collector_number": collector_number,
                "has_set_data": True
            })
            continue
        """
        FORMATO SIMPLES

        Exemplos:
        1 Arcane Signet
        2x Sol Ring
        """
        simple_match = re.match(
            r"(\d+)x?\s+(.+)",
            linha,
            re.IGNORECASE
        )
        if simple_match:

            quantidade = int(simple_match.group(1))
            nome = simple_match.group(2).strip()
            cartas.append({
                "qty": quantidade,
                "name": nome,
                "set": None,
                "collector_number": None,
                "has_set_data": False
            })
            continue
        # linha inválida
        print(f"[PARSER] Linha ignorada: {linha}")

    return cartas