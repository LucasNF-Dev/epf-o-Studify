% rebase("layout.tpl")

<h2>Flashcards</h2>

<a href="/flashcards/novo">+ Criar novo Flashcard</a><br>
<a href="/flashcards/revisar">Revisar Agora</a><br><br>

% if defined('mensagem') and mensagem:
    <p style="color: green; font-weight: bold;"><i>{{mensagem}}</i></p>
% end

% if flashcards:
    <ul>
    % for c in flashcards:
        <li><b>{{c.pergunta}}</b> - <i>{{c.categoria}}</i></li>
    % end
    </ul>
% else:
    <p>Nenhum flashcard cadastrado ainda.</p>
% end
