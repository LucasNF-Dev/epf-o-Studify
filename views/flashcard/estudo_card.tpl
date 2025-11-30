% rebase("layout.tpl")

<h3>Flashcard {{atual}} / {{total}}</h3>

<p><b>Pergunta:</b> {{card.pergunta}}</p>

<button onclick="toggle()">Mostrar Resposta</button>

<p id="resp" style="display:none;">
    <b>Resposta:</b><br>
    {{card.resposta}}
</p>

<br>
<a href="/flashcards/estudar/proximo">Próximo</a>

<script>
function toggle() {
    let el = document.getElementById("resp");
    el.style.display = (el.style.display === "none") ? "block" : "none";
}
</script>
