% rebase('layout', title='Login')

<section style="display: flex; justify-content: center; align-items: center; height: 100vh; background: #f5f5f5;">
  
  <div style="background: white; padding: 40px; border-radius: 10px; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1); width: 100%; max-width: 400px;">
    <h1 style="text-align: center; margin-bottom: 30px; color: #333;">Login</h1>
    
    % if error:
    <div style="background: #f8d7da; color: #721c24; padding: 12px; border-radius: 5px; margin-bottom: 20px; border: 1px solid #f5c6cb;">
      {{ error }}
    </div>
    % end

    <form action="/login" method="post">

      <div style="margin-bottom: 20px;">
        <input type="email" id="email" name="email" required placeholder="Email" 
               style="width: 100%; padding: 12px; border: 1px solid #ddd; border-radius: 5px; font-size: 16px; box-sizing: border-box;"
               value="{{ email or '' }}">
      </div>

      <div style="margin-bottom: 20px;">
        <input type="password" id="password" name="password" required placeholder="Senha" 
               style="width: 100%; padding: 12px; border: 1px solid #ddd; border-radius: 5px; font-size: 16px; box-sizing: border-box;">
      </div>

      <div style="display: flex; justify-content: center; gap: 10px;">
        <button type="submit" style="background: #007bff; color: white; padding: 12px 30px; border: none; border-radius: 5px; cursor: pointer; flex: 1; box-sizing: border-box;">
          Entrar
        </button>
        
        <a href="/register" style="background: #6c757d; color: white; padding: 12px 30px; border: none; border-radius: 5px; cursor: pointer; text-align: center; display: inline-block; flex: 1; box-sizing: border-box; text-decoration: none;">
          Cadastrar
        </a>
      </div>
    </form>
  </div>
</section>