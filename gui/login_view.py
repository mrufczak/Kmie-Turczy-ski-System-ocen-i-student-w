import tkinter as tk
from tkinter import messagebox
from core.auth_manager import AuthManager

class LoginWindow:
    def __init__(self, root, on_login_success):
        self.root = root
        self.on_login_success = on_login_success
        self.auth = AuthManager() 
        
        self.setup_ui()

    def setup_ui(self):
        self.root.title("System Ocen - Logowanie")
        self.root.geometry("800x600")
        self.root.resizable(False, False)

        frame = tk.Frame(self.root, padx=20, pady=20)
        frame.pack(expand=True)


        tk.Label(frame, text="Login:").pack(anchor="w")
        self.entry_login = tk.Entry(frame)
        self.entry_login.pack(fill="x", pady=(0, 10))

        tk.Label(frame, text="Hasło:").pack(anchor="w")
        self.entry_password = tk.Entry(frame, show="*")
        self.entry_password.pack(fill="x", pady=(0, 20))

        btn_login = tk.Button(frame, text="Zaloguj się", command=self.handle_login, bg="#dddddd")
        btn_login.pack(fill="x", ipady=5)

        self.root.bind('<Return>', lambda event: self.handle_login())

    def handle_login(self):
        login = self.entry_login.get()
        password = self.entry_password.get()

        user = self.auth.login(login, password)

        if user:
            self.on_login_success(user)  
        else:
            messagebox.showerror("Błąd", "Niepoprawny login lub hasło!")
            self.entry_password.delete(0, tk.END)