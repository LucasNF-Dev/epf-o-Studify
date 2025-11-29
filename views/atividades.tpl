% rebase('layout.tpl', title='Atividades')


<h1>Atividades</h1>
<a href="/atividades/add">Adicionar Atividade</a>
<table border="1">
    <tr>
        <th>ID</th><th>Nome</th><th>Descrição</th><th>Data</th><th>Feita?</th><th>Ações</th>
    </tr>
    % for a in atividades:
    <tr>
        <td>{{a.id}}</td>
        <td>{{a.nome}}</td>
        <td>{{a.descricao}}</td>
        <td>{{a.data}}</td>
        <td>{{'Sim' if a.feita else 'Não'}}</td>
        <td>
            <a href="/atividades/edit/{{a.id}}">Editar</a>
            <form action="/atividades/delete/{{a.id}}" method="post" style="display:inline;">
                <button type="submit">Excluir</button>
            </form>
        </td>
    </tr>
    % end
</table>