# services/user_service.py (ATUALIZADO)

import bcrypt # NOVO IMPORT
from models.user import UserModel, User

class UserService:
    def __init__(self):
        self.user_model = UserModel()

    # --- Funções Auxiliares de Hashing ---
    
    def _hash_password(self, password: str) -> str:
        """Gera o hash da senha usando bcrypt."""
        # Codifica a senha para bytes (necessário pelo bcrypt)
        password_bytes = password.encode('utf-8')
        # Gera um salt e o hash em uma única chamada
        hashed_bytes = bcrypt.hashpw(password_bytes, bcrypt.gensalt())
        # Retorna o hash como uma string decodificada
        return hashed_bytes.decode('utf-8')

    def _check_password(self, password: str, hashed_password: str) -> bool:
        """Verifica se a senha em texto puro corresponde ao hash."""
        # Codifica a senha e o hash armazenado para bytes
        password_bytes = password.encode('utf-8')
        hashed_bytes = hashed_password.encode('utf-8')
        # Verifica a correspondência
        return bcrypt.checkpw(password_bytes, hashed_bytes)

    # --- Métodos do Serviço ---

    def get_all(self):
        return self.user_model.get_all()

    def get_by_id(self, user_id: int):
        return self.user_model.get_by_id(user_id)

    def login(self, email: str, password: str):
        """Autentica um usuário usando email e verifica o hash da senha."""
        users = self.user_model.get_all()
        
        # 1. Encontra o usuário pelo email
        user = next((u for u in users if u.email == email), None)
        
        if user and user.password:
            # 2. Verifica a senha usando a função de hashing
            if self._check_password(password, user.password):
                return user
                
        return None

    def register(self, name: str, email: str, birthdate: str, password: str):
        """Cria e salva um novo usuário com a senha hasheada."""
        # 1. Validação (mantida)
        if not all([name, email, birthdate, password]):
            raise ValueError("Todos os campos de registro são obrigatórios.")
        
        if any(u.email == email for u in self.user_model.get_all()):
            raise ValueError(f"O email '{email}' já está em uso.")

        # 2. HASH DA SENHA AQUI
        hashed_password = self._hash_password(password) # <-- HASHED!

        # 3. Gera novo ID e salva
        last_id = max([u.id for u in self.user_model.get_all()], default=0)
        new_id = last_id + 1
        
        # Passamos o HASHED_PASSWORD em vez da senha original
        user = User(id=new_id, name=name, email=email, birthdate=birthdate, password=hashed_password)
        self.user_model.add_user(user)
        return user
    
    # ... (outros métodos omitidos)