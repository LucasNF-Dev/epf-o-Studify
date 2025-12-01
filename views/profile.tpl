% rebase('layout', title='Meu Perfil')

<section style="display: flex; justify-content: center; padding: 40px; background: #f5f5f5; min-height: 100vh;">
  <div style="background: white; padding: 30px; border-radius: 10px; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1); width: 100%; max-width: 500px;">
    
    <h1 style="color: #6a0dad; margin-bottom: 25px; text-align: center;">👤 Configurações do Perfil</h1>

    <div style="border-bottom: 1px solid #ddd; padding-bottom: 15px; margin-bottom: 15px;">
        <h3 style="color: #333;">Dados Pessoais</h3>
    </div>
    
    <p><strong>Nome:</strong> {{ user['name'] }}</p>
    <p><strong>Email:</strong> {{ user['email'] }}</p>
    <p><strong>Data de Nascimento:</strong> {{ user['birthdate'] }}</p>
    
    <div style="margin-top: 30px; text-align: center;">
        
        <a href="/users/edit/{{ user['id'] }}" 
           style="background: #007bff; color: white; padding: 10px 20px; border-radius: 5px; text-decoration: none; display: inline-block;">
           Editar Informações
        </a>
        
        <a href="/studify" 
           style="background: #6c757d; color: white; padding: 10px 20px; border-radius: 5px; text-decoration: none; display: inline-block; margin-left: 10px;">
           Voltar ao Dashboard
        </a>
    </div>
    
  </div>
</section>