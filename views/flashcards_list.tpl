% rebase('layout', title='Meus Flashcards')
<%
from datetime import datetime
import time 
%>

<section style="padding: 40px; max-width: 900px; margin: 0 auto; min-height: 100vh;">
    <h1 style="color: #6a0dad; margin-bottom: 20px;">📚 Banco de Flashcards</h1>

    <div style="display: flex; justify-content: space-between; margin-bottom: 30px; gap: 10px;">
        <a href="/flashcards/add" 
           style="background: #28a745; color: white; padding: 10px 20px; border-radius: 5px; text-decoration: none; display: inline-block;">
            ➕ Criar Novo Cartão
        </a>
        <a href="/flashcards/review" 
           style="background: #007bff; color: white; padding: 10px 20px; border-radius: 5px; text-decoration: none; display: inline-block;">
            🧠 Iniciar Revisão ({{ len([c for c in cards if c.due_date <= int(time.time())]) if defined('cards') else 0 }} para hoje)
        </a>
    </div>

    % if not cards:
    <p style="color: #555; text-align: center; padding: 50px; border: 1px dashed #ddd; border-radius: 5px;">
        Você ainda não tem nenhum flashcard! Crie um para começar a estudar.
    </p>
    % else:
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 20px;">
        % for card in cards:
        <div style="background: white; padding: 15px; border-radius: 8px; box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05); border-left: 5px solid #6a0dad;">
            <h4 style="margin-bottom: 8px; color: #333;">{{ card.front[:50] }}{{ '...' if len(card.front) > 50 else '' }}</h4>
            
            <p style="font-size: 14px; color: #777;">
                Próxima Revisão: 
                % if card.due_date <= int(time.time()):
                    <strong style="color: #d9534f;">HOJE!</strong>
                % else:
                    {{ datetime.fromtimestamp(card.due_date).strftime('%d/%m/%Y') }}
                % end
            </p>
            <p style="font-size: 14px; color: #777; margin-bottom: 15px;">
                Intervalo: {{ card.interval }} dias | Facilidade (EF): {{ '%.2f' % card.ease }}
            </p>
            
            <div style="margin-top: 10px; display: flex; justify-content: flex-end; gap: 10px; border-top: 1px solid #eee; padding-top: 10px;">
                
                <a href="/flashcards/edit/{{ card.id }}" style="color: #007bff; text-decoration: none; font-weight: bold; font-size: 0.9em;">
                    Editar
                </a>

                <form method="POST" action="/flashcards/delete/{{ card.id }}" style="margin: 0;">
                    <button type="submit" onclick="return confirm('Tem certeza que deseja excluir este cartão?')" 
                            style="background: none; border: none; color: #dc3545; padding: 0; font-weight: bold; font-size: 0.9em; cursor: pointer;">
                        Excluir
                    </button>
                </form>
            </div>
            </div>
        % end
    </div>
    % end
</section>