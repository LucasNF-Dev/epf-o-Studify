% rebase("layout.tpl)

<h2>Calendario</h2>

<a href="/calendario/prova/nova">+ Adicionar Prova</a>
<br>
<a href="/calendario/evento/novo">+ Adicionar Evento</a>

<h3>Provas</h3>% for p in calendario.provas:
% for p in calendario.provas:
    <p><b>{{p.data}}</b> - {{p.materia}}</p>
% end

<h3>Eventos</h3>
% for e in calendario.eventos;
    <p><b>{{e.data}}</b> - {{e.titulo}}<br>{{e.descricao}}</p>
% end 