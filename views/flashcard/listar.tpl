% rebase("layout.tpl")

<h2>Flashcards</h2>

<a href="/flashcards/novo">+ Criar novo Flashcard</a>

<ul>
% for c in flashcards:
    <li><b>{{c.pergunta}}</b></li>
% end 
</ul>