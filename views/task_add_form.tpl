% rebase('layout', title='Adicionar Tarefa')

<section style="display: flex; justify-content: center; align-items: flex-start; padding: 40px; min-height: 100vh; background: #f5f5f5;">
    <div style="background: white; padding: 40px; border-radius: 10px; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1); width: 100%; max-width: 500px;">
        <h1 style="text-align: center; margin-bottom: 30px; color: #6a0dad;">➕ Nova Tarefa de Estudo</h1>

        % if error:
        <div style="background: #f8d7da; color: #721c24; padding: 12px; border-radius: 5px; margin-bottom: 20px; border: 1px solid #f5c6cb;">
            {{ error }}
        </div>
        % end

        <form action="/tasks/add" method="post">
            
            <div style="margin-bottom: 20px;">
                <label for="title" style="display: block; margin-bottom: 5px; color: #555;">Título da Tarefa</label>
                <input type="text" id="title" name="title" value="{{ title or '' }}" required
                       style="width: 100%; padding: 10px; border: 1px solid #ddd; border-radius: 5px; font-size: 16px; box-sizing: border-box;">
            </div>

            <div style="margin-bottom: 30px;">
                <label for="description" style="display: block; margin-bottom: 5px; color: #555;">Descrição (Opcional)</label>
                <textarea id="description" name="description" rows="4"
                       style="width: 100%; padding: 12px; border: 1px solid #ddd; border-radius: 5px; font-size: 16px; box-sizing: border-box;">{{ description or '' }}</textarea>
            </div>

            <div style="display: flex; justify-content: center; gap: 15px;">
                <button type="submit" style="background: #007bff; color: white; padding: 12px 30px; border: none; border-radius: 5px; cursor: pointer; flex: 1;">
                    Salvar Tarefa
                </button>
                <a href="/tasks" style="background: #6c757d; color: white; padding: 12px 30px; border-radius: 5px; text-decoration: none; text-align: center; flex: 1;">
                    Cancelar
                </a>
            </div>
        </form>
    </div>
</section>