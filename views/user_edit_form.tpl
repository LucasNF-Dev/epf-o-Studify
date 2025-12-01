% rebase('layout', title='Editar Perfil')

<section style="display: flex; justify-content: center; align-items: center; min-height: 100vh; background: #f5f5f5;">
<div style="background: white; padding: 40px; border-radius: 10px; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1); width: 100%; max-width: 450px;">
<h1 style="text-align: center; margin-bottom: 30px; color: #6a0dad;">Editar Perfil</h1>

% if error:
<div style="background: #f8d7da; color: #721c24; padding: 12px; border-radius: 5px; margin-bottom: 20px; border: 1px solid #f5c6cb;">
{{ error }}
</div>
% end

<form action="/users/edit/{{ user_id }}" method="post">
    <div style="margin-bottom: 20px;">
        <label for="name" style="display: block; margin-bottom: 5px; color: #555;">Nome</label>
        <input type="text" id="name" name="name" required 
               style="width: 100%; padding: 12px; border: 1px solid #ddd; border-radius: 5px; box-sizing: border-box;"
               value="{{ name or '' }}">
    </div>

    <div style="margin-bottom: 20px;">
        <label for="email" style="display: block; margin-bottom: 5px; color: #555;">Email</label>
        <input type="email" id="email" name="email" required 
               style="width: 100%; padding: 12px; border: 1px solid #ddd; border-radius: 5px; box-sizing: border-box;"
               value="{{ email or '' }}">
    </div>
    
    <div style="margin-bottom: 20px;">
        <label for="birthdate" style="display: block; margin-bottom: 5px; color: #555;">Data de Nascimento</label>
        <input type="date" id="birthdate" name="birthdate" required 
               style="width: 100%; padding: 12px; border: 1px solid #ddd; border-radius: 5px; box-sizing: border-box;"
               value="{{ birthdate or '' }}">
    </div>

    <hr style="margin: 30px 0;">

    <div style="margin-bottom: 20px;">
        <label for="new_password" style="display: block; margin-bottom: 5px; color: #555;">Nova Senha (deixe em branco para não mudar)</label>
        <input type="password" id="new_password" name="new_password" placeholder="Mínimo 6 caracteres"
               style="width: 100%; padding: 12px; border: 1px solid #ddd; border-radius: 5px; box-sizing: border-box;">
    </div>

    <div style="display: flex; justify-content: space-between; gap: 10px;">
        <button type="submit" style="background: #28a745; color: white; padding: 12px 30px; border: none; border-radius: 5px; cursor: pointer; flex: 1;">
            Salvar Alterações
        </button>
        <a href="/users/profile" style="background: #6c757d; color: white; padding: 12px 30px; border: none; border-radius: 5px; cursor: pointer; text-align: center; display: inline-block; flex: 1; text-decoration: none;">
            Cancelar
        </a>
    </div>
</form>
</div>
</section>