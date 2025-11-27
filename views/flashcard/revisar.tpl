% rebase("layout.tpl")

<h2>Revisar Flashcard</h2>

<p><b>Pergunta:</b> {{card.pergunta}}</p>

<p><details><summary>Mostrar Resposta</summary>
    {{card.resposta}}

</details></p>

<h3>Como foi?</h3>

<a href="/flashcards/revisar/{{card.id}}/1">Fácil (+3 dias)</a><br>
<a href="/flashcards/revisar/{{card.id}}/2">Médio (+2 dias)</a><br>
<a href="/flashcards/revisar/{{card.id}}/3">Difícil (+1 dia)</a>