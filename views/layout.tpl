<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ title or 'Studify - App de Estudos' }}</title>
    <link rel="stylesheet" href="/static/css/style.css">
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap" rel="stylesheet">
</head>
<body>

    <header>
        <div class="container">
            <h1><a href="/">📚 Studify</a></h1>
            <nav>
                <ul>
                    <li><a href="/flashcards">Flashcards</a></li>
                    <li><a href="/calendario">Calendário</a></li>
                    <li><a href="/logout">Sair</a></li>
                </ul>
            </nav>
        </div>
    </header>
    
    <main class="container">
        {{!base}} 
    </main>

    <footer>
        <div class="container">
            <p>&copy; 2025 Studify - Projeto POO UnB</p>
        </div>
    </footer>
    
</body>
</html>