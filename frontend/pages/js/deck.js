const btnNovoDeck = document.getElementById("btnNovoDeck");
const modal = document.getElementById("modalDeck");
const fechar = document.getElementById("fecharModal");

btnNovoDeck.addEventListener("click", () => {
    modal.classList.remove("hidden");
});

fechar.addEventListener("click", () => {
    modal.classList.add("hidden");
});