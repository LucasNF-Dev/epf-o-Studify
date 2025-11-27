% rebase('layout', title='Formulário Usuário')

<section style="display: flex; justify-content: center; align-items: center; height: 100vh; background: #f5f5f5;">
    <div style="background: white; padding: 40px; border-radius: 10px; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1); width: 100%; max-width: 400px;">
        
        <h1 style="text-align: center; margin-bottom: 30px; color: #333;">{{'Editar Usuário' if user else 'Adicionar Usuário'}}</h1>
        
        <form action="{{action}}" method="post" class="form-container">
            
            <div class="form-group" style="margin-bottom: 20px;">
                <input type="text" id="name" name="name" required 
                       value="{{user.name if user else ''}}" placeholder="Nome" style="width: 100%; padding: 12px; border: 1px solid #ddd; border-radius: 5px; font-size: 16px; box-sizing: border-box;">
            </div>
            
            <div class="form-group" style="margin-bottom: 20px;">
                <input type="email" id="email" name="email" required 
                       value="{{user.email if user else ''}}" placeholder="Email" style="width: 100%; padding: 12px; border: 1px solid #ddd; border-radius: 5px; font-size: 16px; box-sizing: border-box;">
            </div>
            
            <div class="form-group" style="margin-bottom: 20px;">
                <input type="password" id="password" name="password" required
                        value="{{user.password if user else ''}}" placeholder="Senha" style="width: 100%; padding: 12px; border: 1px solid #ddd; border-radius: 5px; font-size: 16px; box-sizing: border-box;">
            </div>
            
            <div class="form-group" style="margin-bottom: 25px;">
                <input type="date" id="birthdate" name="birthdate" required 
                       value="{{user.birthdate if user else ''}}" style="width: 100%; padding: 12px; border: 1px solid #ddd; border-radius: 5px; font-size: 16px; box-sizing: border-box;">
            </div>

            <div class="form-actions" style="display: flex; gap: 10px; justify-content: center;">
                <button type="submit" class="btn-submit" style="flex: 1; max-width: 120px; padding: 12px; background: #007bff; color: white; border: none; border-radius: 5px; cursor: pointer;">Salvar</button>
                <a href="/users" class="btn-cancel" style="flex: 1; max-width: 120px; padding: 12px; background: #6c757d; color: white; text-decoration: none; border-radius: 5px; text-align: center; display: block;">Voltar</a>
            </div>
        </form>
    </div>
</section>