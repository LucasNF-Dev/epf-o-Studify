% rebase('layout', title='Quadro Kanban')

<section style="padding: 40px; max-width: 1200px; margin: 0 auto; min-height: 100vh;">
    <h1 style="color: #6a0dad; margin-bottom: 20px;">📋 Quadro Kanban (Estudos)</h1>

    <div style="display: flex; justify-content: space-between; margin-bottom: 30px;">
        <a href="/tasks/add" 
           style="background: #28a745; color: white; padding: 10px 20px; border-radius: 5px; text-decoration: none; display: inline-block;">
            ➕ Adicionar Nova Tarefa
        </a>
        <a href="/studify" 
           style="background: #6c757d; color: white; padding: 10px 20px; border-radius: 5px; text-decoration: none; display: inline-block;">
            Voltar ao Dashboard
        </a>
    </div>

    <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 20px;">
        
        % for status_key, status_name in column_names.items():
        <div style="background: #f4f4f9; padding: 15px; border-radius: 8px; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);">
            <h2 style="margin-bottom: 20px; font-size: 1.5em; color: #333; border-bottom: 2px solid #ddd;">{{ status_name }} ({{ len(board[status_key]) }})</h2>
            
            <div style="display: flex; flex-direction: column; gap: 10px;">
                
                % if not board[status_key]:
                <p style="color: #999; text-align: center; padding: 20px;">Nenhuma tarefa nesta coluna.</p>
                % end

                % for task in board[status_key]:
                <div style="background: white; padding: 15px; border-radius: 5px; border-left: 5px solid {{ '#007bff' if task.status == STATUS_TODO else ('#f0ad4e' if task.status == STATUS_IN_PROGRESS else '#5cb85c') }}; box-shadow: 0 1px 3px rgba(0, 0, 0, 0.05);">
                    <h4 style="margin-bottom: 5px; color: #333;">{{ task.title }}</h4>
                    % if task.description:
                    <p style="font-size: 0.9em; color: #777; margin-bottom: 10px;">{{ task.description[:80] }}</p>
                    % end
                    
                    <div style="display: flex; justify-content: space-between; margin-top: 10px; font-size: 0.8em;">
                        
                        % if status_key == STATUS_IN_PROGRESS or status_key == STATUS_DONE:
                        <form method="POST" action="/tasks/move/{{ task.id }}" style="margin: 0;">
                            <input type="hidden" name="new_status" value="{{ STATUS_TODO if status_key == STATUS_IN_PROGRESS else STATUS_IN_PROGRESS }}">
                            <button type="submit" style="background: none; border: none; color: #555; cursor: pointer;">&#9664; Anterior</button>
                        </form>
                        % end

                        % if status_key == STATUS_TODO or status_key == STATUS_IN_PROGRESS:
                        <form method="POST" action="/tasks/move/{{ task.id }}" style="margin: 0;">
                            <input type="hidden" name="new_status" value="{{ STATUS_IN_PROGRESS if status_key == STATUS_TODO else STATUS_DONE }}">
                            <button type="submit" style="background: none; border: none; color: #5cb85c; cursor: pointer;">Próximo &#9654;</button>
                        </form>
                        % end
                    </div>
                </div>
                % end
            </div>
        </div>
        % end
        
    </div>
</section>