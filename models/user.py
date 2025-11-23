import os
import json
import bcrypt
import logging
from dataclasses import dataclass, asdict
from typing import List

logger = logging.getLogger(__name__)

DATA_DIR = os.path.join(os.path.dirname(__file__), '..', 'data')

class User:
    def __init__(self, id, name, email, birthdate, password, is_hashed=False):
        self.id = id
        self.name = name
        self.email = email
        self.birthdate = birthdate
        if is_hashed:
            self.password = password
        else:
            self.password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode()


    def __repr__(self):
        return (f"User(id={self.id}, name='{self.name}', email='{self.email}', "
                f"birthdate='{self.birthdate}')")
    

    def verify_password(self, password) -> bool:
        try:
            return bcrypt.checkpw(password.encode('utf-8'), self.password.encode('utf-8'))
        except Exception as e:
            logger.error(f"Erro ao verificar a senha: {e}")
            return False


    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'birthdate': self.birthdate,
            'password' : self.password
        }


    @classmethod
    def from_dict(cls, data):
        return cls(
            id=data['id'],
            name=data['name'],
            email=data['email'],
            birthdate=data['birthdate'],
            password=data['password'],
            is_hashed=True
        )


class UserModel:
    FILE_PATH = os.path.join(DATA_DIR, 'users.json')

    def __init__(self):
        self.users = self._load()


    def _load(self):
        if not os.path.exists(self.FILE_PATH):
            return []
        with open(self.FILE_PATH, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return [User.from_dict(item) for item in data]


    def _save(self):
        with open(self.FILE_PATH, 'w', encoding='utf-8') as f:
            json.dump([u.to_dict() for u in self.users], f, indent=4, ensure_ascii=False)


    def get_all(self):
        return self.users


    def get_by_email(self, user_email: str):
        return next((u for u in self.users if u.email == user_email), None)
    
    
    def get_by_id(self, user_id: int):
        return next((u for u in self.users if u.id == user_id), None)


    def add_user(self, user: User):
        self.users.append(user)
        self._save()


    def update_user(self, updated_user: User):
        for i, user in enumerate(self.users):
            if user.id == updated_user.id:
                self.users[i] = updated_user
                self._save()
                break


    def delete_user(self, user_id: int):
        self.users = [u for u in self.users if u.id != user_id]
        self._save()

    def login(self, user_email: str, user_password: str):
        user = self.get_by_email(user_email)

        if not user:
            logger.warning(f"Email não cadastrado!")
            return None
        
        if user.verify_password(user_password):
            return user
        else:
            logger.warning(f"Senha incorreta!")
            return None
