% rebase("layout.tpl")

<h2>Flashcards</h2>

<a href="/flashcards/novo">+ Criar novo Flashcard</a><br>
<a href="/flashcards/revisar">Revisar Agora</a><br><br>
<a href="/flashcards/estudar" style="font-weight: bold;">Modo de Estudo</a><br><br>

% if defined('mensagem') and mensagem:
    <p style="color: green; font-weight: bold;"><i>{{mensagem}}</i></p>
% end

% if flashcards:
    <ul>
    % for c in flashcards:
        <li>
            <b>{{c.pergunta}}</b> — <i>{{c.categoria}}</i>
            <br>
            <a href="/flashcards/{{c.id}}/editar">Editar</a> |
            <a href="/flashcards/{{c.id}}/excluir" onclick="return confirm('Tem certeza que deseja excluir?')">Excluir</a>
        </li>
        <br>
    % end
    </ul>
% else:
    <p>Nenhum flashcard cadastrado ainda.</p>
% end
