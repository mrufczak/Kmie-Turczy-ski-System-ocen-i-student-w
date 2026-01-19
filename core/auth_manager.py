import json
import hashlib
import os

class AuthManager:
    def __init__(self, db_path='data/users.json'):
        self.db_path = db_path
        self.users = self._load_users()

    def _load_users(self):
        if not os.path.exists(self.db_path): 
            print(f"BŁĄD: Nie znaleziono pliku {self.db_path}")
            return -1
        
        try:
            with open(self.db_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except json.JSONDecodeError:
            print("BŁĄD: Plik users.json jest uszkodzony")
            return -2

    def _hash_password(self, password):
        return hashlib.md5(password.encode('utf-8')).hexdigest()

    def login(self, login, password):
        user_data = self.users.get(login)

        if not user_data:
            return None

        stored_hash = user_data.get('password_hash')
        provided_hash = self._hash_password(password)

        if stored_hash == provided_hash:
            return {
                "login": login,
                "role": user_data['role'],
                "first_name": user_data.get('first_name'),
                "last_name": user_data.get('last_name'),
                "index_number": user_data.get('index_number') 
            }
        else:
            return None  