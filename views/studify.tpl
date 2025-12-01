% rebase('layout.tpl', title='Studify - Dashboard')
<% data = defined('data_for_view') and data_for_view or {} %>

<style>
    /* Estilos de Reset e Centralização */
    .dashboard-container {
        padding: 40px 20px;
        max-width: 1100px;
        margin: 0 auto; /* Centraliza o conteúdo */
        font-family: Arial, sans-serif;
    }

    /* Cabeçalho e Saída */
    .dashboard-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 30px;
        border-bottom: 2px solid #ddd;
        padding-bottom: 15px;
    }

    .dashboard-header h1 {
        color: #1a1a1a;
        font-size: 2.2em;
        margin: 0;
    }

    /* Mensagem de boas-vindas */
    .welcome-info {
        color: #555;
        margin-bottom: 40px;
        font-size: 1.1em;
    }

    /* Container dos Cards (usa Flexbox/Grid moderno) */
    .feature-cards-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
        gap: 25px; /* Espaçamento mais limpo */
    }

    /* Estilo do Card Individual */
    .feature-card {
        background: white;
        padding: 30px;
        border-radius: 12px; /* Bordas mais suaves */
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.08); /* Sombra suave */
        text-decoration: none;
        color: #333;
        display: block;
        transition: transform 0.2s ease, box-shadow 0.2s ease;
    }

    .feature-card:hover {
        transform: translateY(-5px); /* Efeito de elevação sutil */
        box-shadow: 0 8px 25px rgba(0, 0, 0, 0.15); /* Sombra mais pronunciada */
    }

    .feature-card h2 {
        font-size: 1.6em;
        margin-bottom: 10px;
        font-weight: 600;
    }

    .feature-card p {
        color: #666;
        font-size: 0.95em;
        margin-bottom: 0;
    }

    /* Cores de Destaque */
    .flashcards-icon { color: #007bff; }
    .schedule-icon { color: #28a745; }
    .profile-icon { color: #6f42c1; }

    /* Estilo do Botão Sair */
    .logout-link {
        color: #dc3545 !important;
        font-weight: 600;
        text-decoration: none;
        transition: color 0.2s;
        padding: 8px 15px;
        border: 1px solid #dc3545;
        border-radius: 5px;
    }

    .logout-link:hover {
        background-color: #dc3545;
        color: white !important;
    }

    /* Responsividade */
    @media (max-width: 600px) {
        .dashboard-header {
            flex-direction: column;
            align-items: flex-start;
        }
        .dashboard-header h1 {
            margin-bottom: 15px;
        }
        .feature-cards-grid {
            grid-template-columns: 1fr; /* Pilha os cartões em telas menores */
        }
    }
</style>

<section style="background: #f5f5f5; min-height: 100vh;">

    <div class="dashboard-container">

        <div class="dashboard-header">
            <h1>Bem-vindo(a), {{ data.get('user_name', 'Usuário') }}!</h1>
            <a href="/logout" class="logout-link">Sair</a>
        </div>

        <p class="welcome-info">
            O que você quer estudar hoje? Você tem **{{ data.get('total_flashcards', '0') }}** flashcards cadastrados e **{{ data.get('upcoming_events', '0') }}** eventos agendados.
        </p>

        <div class="feature-cards-grid">
            
            <a href="/flashcards" class="feature-card">
                <h2 class="flashcards-icon">📚 Flashcards</h2>
                <p>Crie revisões rápidas e personalize seus estudos.</p>
                <p style="margin-top: 10px; font-weight: bold;">{{ data.get('total_flashcards', '0') }} Cadastrados</p>
            </a>

            <a href="/schedule" class="feature-card">
                <h2 class="schedule-icon">🗓️ Cronograma</h2>
                <p>Próxima atividade: **{{ data.get('next_event', 'Nenhuma agendada') }}**.</p>
                <p style="margin-top: 10px;">Gerencie horários e tarefas.</p>
            </a>

            <a href="/users/profile" class="feature-card">
                <h2 class="profile-icon">👤 Perfil</h2>
                <p>Gerencie suas informações e configurações do sistema.</p>
                <p style="margin-top: 10px;">Acessar Configurações</p>
            </a>

        </div>

    </div>

</section>