% rebase('layout', title='Formulário Usuário')

<section class="form-section">
    <h1>{{'Editar Usuário' if user else 'Adicionar Usuário'}}</h1>
    
    <form action="{{action}}" method="post" class="form-container">
        
        <div class="form-group">
            <input type="text" id="name" name="name" required 
                   value="{{user.name if user else ''}}" placeholder="Nome">
        </div>
        
        <div class="form-group">
            <input type="email" id="email" name="email" required 
                   value="{{user.email if user else ''}}" placeholder="Email">
        </div>
        
        <div class="form-group">
            <input type="password" id="password" name="password" required
                    value="{{user.password if user else ''}}" placeholder="Senha">
        </div>
        
        <div class="form-group">
            <input type="date"  id="birthdate" name="birthdate" required 
                   value="{{user.birthdate if user else ''}}" placeholder="Data de Nascimento">
        </div>

        <div class="form-actions">
            <button type="submit" class="btn-submit">Salvar</button>
            <a href="/users" class="btn-cancel">Voltar</a>
        </div>
    </form>
</section>