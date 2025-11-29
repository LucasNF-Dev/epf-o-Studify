% rebase('layout.tpl', title='Nova Atividade' if not atividade else 'Editar Atividade')


<h1>{{'Editar Atividade' if atividade else 'Nova Atividade'}}</h1>
<form action="{{action}}" method="post">
    <label>Nome:<br>
        <input type="text" name="nome" value="{{atividade.nome if atividade else ''}}" required>
    </label><br><br>
    <label>Descrição:<br>
        <textarea name="descricao" required>{{atividade.descricao if atividade else ''}}</textarea>
    </label><br><br>
    <label>Data:<br>
        <input type="date" name="data" value="{{atividade.data if atividade else ''}}" required>
    </label><br><br>
    <label>
        <input type="checkbox" name="feita" % if atividade and atividade.feita %checked% end>
        Feita?
    </label><br><br>
    <button type="submit">Salvar</button>
</form>
<a href="/atividades">Voltar</a>