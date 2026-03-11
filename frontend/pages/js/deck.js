const btnNovoDeck = document.getElementById("btnNovoDeck");
const modal = document.getElementById("modalDeck");
const fechar = document.getElementById("fecharModal");

btnNovoDeck.addEventListener("click", () => {
    modal.classList.remove("hidden");
});

fechar.addEventListener("click", () => {
    modal.classList.add("hidden");
});

async function salvarDeck(){

    const nome = document.getElementById("deckName").value
    const commander = document.getElementById("deckCommander").value
    const lista = document.getElementById("deckList").value

    const deck = {

        name: nome,
        commander: commander,
        list: lista

    }

    await window.pywebview.api.salvarDeck(deck)

}