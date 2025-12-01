% rebase("layout.tpl", title='Editar Cards')

<h2>Editar Flashcard</h2>

<form method="post">

    <label>Pergunta:</label><br>
    <input type="text" name="pergunta" value="{{flashcard.pergunta}}"><br><br>

    <label>Resposta:</label><br>
    <textarea name="resposta">{{flashcard.resposta}}</textarea><br><br>

    <label>Categoria:</label><br>
    <select name="categoria">
        % for c in categorias:
            <option value="{{c}}" {{ "selected" if c == flashcard.categoria else "" }}>{{c}}</option>
        % end
    </select>

    <br><br>
    <button type="submit">Salvar</button>
</form>
