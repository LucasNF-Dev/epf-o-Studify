import bcrypt
from models.user import UserModel, User

class UserService:
    def __init__(self):
        self.user_model = UserModel()

    # --- Funções Auxiliares de Hashing ---
    
    def _hash_password(self, password: str) -> str:
        """Gera o hash da senha usando bcrypt."""
        password_bytes = password.encode('utf-8')
        hashed_bytes = bcrypt.hashpw(password_bytes, bcrypt.gensalt())
        return hashed_bytes.decode('utf-8')

    def _check_password(self, password: str, hashed_password: str) -> bool:
        """Verifica se a senha em texto puro corresponde ao hash."""
        password_bytes = password.encode('utf-8')
        hashed_bytes = hashed_password.encode('utf-8')
        return bcrypt.checkpw(password_bytes, hashed_bytes)

    # --- Métodos do Serviço ---

    def get_all(self):
        return self.user_model.get_all()

    def get_by_id(self, user_id: int):
        return self.user_model.get_by_id(user_id)

    def login(self, email: str, password: str):
        """Autentica um usuário usando email e verifica o hash da senha."""
        users = self.user_model.get_all()
        user = next((u for u in users if u.email == email), None)
        
        if user and user.password:
            if self._check_password(password, user.password):
                return user
                
        return None

    def register(self, name: str, email: str, birthdate: str, password: str):
        """Cria e salva um novo usuário com a senha hasheada."""
        if not all([name, email, birthdate, password]):
            raise ValueError("Todos os campos de registro são obrigatórios.")
        
        if any(u.email == email for u in self.user_model.get_all()):
            raise ValueError(f"O email '{email}' já está em uso.")

        hashed_password = self._hash_password(password)

        last_id = max([u.id for u in self.user_model.get_all()], default=0)
        new_id = last_id + 1
        
        user = User(id=new_id, name=name, email=email, birthdate=birthdate, password=hashed_password)
        self.user_model.add_user(user)
        return user

    def edit_user(self, user, name: str, email: str, birthdate: str, new_password: str = None):
        """Atualiza os dados do usuário, incluindo a senha se fornecida."""
        
        if not all([name, email, birthdate]):
            raise ValueError("Nome, email e data de nascimento são obrigatórios.")

        # 1. Atualizar dados básicos
        user.name = name
        user.email = email
        user.birthdate = birthdate

        # 2. Atualizar senha (se fornecida)
        if new_password:
            if len(new_password) < 6:
                raise ValueError("A nova senha deve ter pelo menos 6 caracteres.")
            
            user.password = self._hash_password(new_password)

        # 3. Salvar no modelo
        self.user_model.update_user(user)

    def delete_user(self, user_id: int):
        self.user_model.delete_user(user_id)