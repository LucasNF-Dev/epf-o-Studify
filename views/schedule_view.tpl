% rebase('layout', title='Cronograma')

<section style="padding: 40px; max-width: 900px; margin: 0 auto; min-height: 100vh;">
    <h1 style="color: #6a0dad; margin-bottom: 30px;">🗓️ Meu Cronograma</h1>

    <div style="display: flex; justify-content: space-between; margin-bottom: 30px; gap: 10px;">
        <a href="/schedule/add" 
           style="background: #28a745; color: white; padding: 10px 20px; border-radius: 5px; text-decoration: none; display: inline-block;">
            ➕ Adicionar Novo Evento
        </a>
        <a href="/studify" 
           style="background: #6c757d; color: white; padding: 10px 20px; border-radius: 5px; text-decoration: none; display: inline-block;">
            Voltar ao Dashboard
        </a>
    </div>

    % if not events:
    <p style="color: #555; text-align: center; padding: 50px; border: 1px dashed #ddd; border-radius: 5px;">
        Nenhum compromisso agendado. Comece adicionando um novo evento!
    </p>
    % else:
    <h2 style="color: #333; margin-bottom: 20px; border-bottom: 2px solid #eee; padding-bottom: 10px;">Próximos Eventos</h2>
    <div style="display: flex; flex-direction: column; gap: 15px;">
        % for event in events:
        <div style="background: white; padding: 15px; border-radius: 8px; box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05); border-left: 5px solid #007bff;">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 5px;">
                <h4 style="margin: 0; color: #333;">{{ event['title'] }}</h4>
                <div style="display: flex; align-items: center; gap: 10px;">
                    <span style="background: #007bff; color: white; padding: 4px 8px; border-radius: 4px; font-size: 12px;">
                        {{ event['start'] }} - {{ event['end'] }}
                    </span>
                    
                    <a href="/schedule/edit/{{ event['id'] }}" title="Editar" style="color: #f0ad4e; text-decoration: none;">
                        &#9998;
                    </a>
                    
                    <form method="POST" action="/schedule/delete/{{ event['id'] }}" style="margin: 0;">
                        <button type="submit" onclick="return confirm('Tem certeza que deseja excluir {{ event['title'] }}?')" 
                                style="background: none; border: none; cursor: pointer; color: #d9534f; padding: 0;">
                            &times;
                        </button>
                    </form>
                </div>
            </div>
            % if event['description']:
            <p style="font-size: 14px; color: #777; margin: 0;">{{ event['description'] }}</p>
            % end
        </div>
        % end
    </div>
    % end
</section>