% rebase('layout', title='Revisão')

<section style="display: flex; justify-content: center; align-items: center; min-height: 100vh; background: #f5f5f5;">
    
    <div style="width: 100%; max-width: 500px; text-align: center; padding: 20px;">

        <h1 style="color: #6a0dad; margin-bottom: 30px;">Revisão Ativa</h1>

        <div style="background: white; padding: 40px; border-radius: 10px; box-shadow: 0 6px 10px rgba(0, 0, 0, 0.15); min-height: 200px; margin-bottom: 30px; border-top: 5px solid #6a0dad;">
            
            <h3 style="color: #333; margin-bottom: 20px;">{{ card.front }}</h3>
            
            % if show_back:
            <hr style="margin: 20px auto; width: 50%;">
            <p style="color: #555; font-size: 18px;">{{ card.back }}</p>
            % end

        </div>

        <form method="POST" action="/flashcards/check/{{ card.id }}" style="display: flex; flex-direction: column; gap: 10px;">
            
            % if not show_back:
            <button type="submit" name="quality" value="-1" 
                    style="background: #007bff; color: white; padding: 15px; border: none; border-radius: 5px; cursor: pointer; font-size: 18px;">
                Mostrar Resposta
            </button>
            % else:
            <p style="color: #555; margin-bottom: 15px;">Como você avalia sua lembrança?</p>
            <div style="display: grid; grid-template-columns: repeat(5, 1fr); gap: 10px;">
                
                <button type="submit" name="quality" value="1" style="background: #d9534f; color: white; padding: 10px; border: none; border-radius: 5px; cursor: pointer;">
                    1. Errei
                </button>
                <button type="submit" name="quality" value="2" style="background: #f0ad4e; color: white; padding: 10px; border: none; border-radius: 5px; cursor: pointer;">
                    2. Difícil
                </button>
                <button type="submit" name="quality" value="3" style="background: #5cb85c; color: white; padding: 10px; border: none; border-radius: 5px; cursor: pointer;">
                    3. Bom
                </button>
                <button type="submit" name="quality" value="4" style="background: #4cc722; color: white; padding: 10px; border: none; border-radius: 5px; cursor: pointer;">
                    4. Fácil
                </button>
                <button type="submit" name="quality" value="5" style="background: #337ab7; color: white; padding: 10px; border: none; border-radius: 5px; cursor: pointer;">
                    5. Muito Fácil
                </button>
            </div>
            % end
        </form>
        <a href="/studify" style="display: block; margin-top: 20px; color: #6c757d; text-decoration: none;">Sair da Revisão</a>
    </div>
</section>