% rebase("layout.tpl", title='Estudo Menu')

<h2>Modo Estudo Completo</h2>

<form method="post">

    <label>Categoria:</label><br>
    <select name="categoria">
        <option value="todas">Todas</option>
        % for c in categorias:
            <option value="{{c}}">{{c}}</option>
        % end
    </select>
    <br><br>

    <label>Quantidade:</label><br>
    <input type="number" name="quantidade" min="1" max="{{total}}" value="{{total}}">
    <br><br>

    <label>Ordem:</label><br>
    <select name="ordem">
        <option value="normal">Normal</option>
        <option value="aleatoria">Aleatória</option>
    </select>

    <br><br>
    <button type="submit">Iniciar Estudo</button>
</form>
