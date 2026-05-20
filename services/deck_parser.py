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
        # ignora sideboard
        if linha.upper().startswith("SB:"):
            continue
        """
        Se não começar com número,
        assume quantidade 1
        """
        if not re.match(r"^\d+", linha):

            linha = f"1 {linha}"
        """
        FORMATO COMPLETO

        1 Arcane Signet (C20) 237
        """
        full_match = re.match(
            r"(\d+)x?\s+(.+?)\s+\(([A-Z0-9]+)\)\s+([A-Z0-9\-\*]+)",
            linha,
            re.IGNORECASE
        )

        if full_match:
            cartas.append({
                "qty": int(full_match.group(1)),
                "name": full_match.group(2).strip(),
                "set": full_match.group(3).lower(),
                "collector_number": full_match.group(4),
                "has_set_data": True
            })

            continue

        """
        FORMATO SIMPLES

        1 Arcane Signet
        2x Sol Ring
        """

        simple_match = re.match(
            r"(\d+)x?\s+(.+)",
            linha,
            re.IGNORECASE
        )

        if simple_match:

            cartas.append({
                "qty": int(simple_match.group(1)),
                "name": simple_match.group(2).strip(),
                "set": None,
                "collector_number": None,
                "has_set_data": False
            })

            continue

        print(f"[PARSER] Linha ignorada: {linha}")
    
    return cartas