% rebase("layout.tpl", title='Novo Flashcard')

<h2>Novo Flashcard</h2>

<form method="post">
    <label>Pergunta:</label><br>
    <input name="pergunta" type="text"><br><br>

    <label>Resposta:</label><br>
    <textarea name="resposta"></textarea><br><br>

    <label>Categoria:</label><br>
    <select name="categoria" id="categoria-select" onchange="toggleOutro()">
        % for c in categorias:
            <option value="{{c}}">{{c}}</option>
        % end 
            <option value="outro">Outro...</option>
    </select>
    <br><br>

    <div id="outro-wrapper" style="display:none;">
        <label>Nova categoria:</label><br>
        <input type="text" name="categoria_nova">
    </div>

    <br>
    <button type="submit">Criar</button>
</form>

<script>
function toggleOutro() {
    let select = document.getElementById("categoria-select");
    let outroDiv = document.getElementById("outro-wrapper");

    if (select.value === "outro") {
        outroDiv.style.display = "block";
    } else {
        outroDiv.style.display = "none";
    }
}
</script>
