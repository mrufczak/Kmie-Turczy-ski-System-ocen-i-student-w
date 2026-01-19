import tkinter as tk
from tkinter import messagebox


from gui.login_view import LoginWindow
# from gui.student_view import StudentView
# from gui.employee_view import EmployeeView

class Application:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("System Obsługi Ocen")
        self.root.geometry("800x600")
        
        self.show_login_screen()

    def run(self):
        """Uruchamia petle programu"""
        self.root.mainloop()

    def _clear_window(self):
        """Czyści okno"""
        for widget in self.root.winfo_children():
            widget.destroy()

    def show_login_screen(self):
        """Wyświetla ekran logowania"""
        self._clear_window()
        self.root.geometry("300x250") 
        

        LoginWindow(self.root, self.on_login_success)

    def on_login_success(self, user):
        """
        Ta funkcja decyduje, który ekran pokazać dalej
        """
        print(f"Zalogowano jako: {user['login']} ({user['role']})")
        
        if user['role'] == 'student':
            self.show_student_screen(user)
        elif user['role'] == 'pracownik':
            self.show_employee_screen(user)
        else:
            messagebox.showerror("Błąd", "Nieznana rola użytkownika!")

    def show_student_screen(self, user):
        """Ładuje widok dla Studenta."""
        self._clear_window()
        
        #StudentView(self.root, user, self.logout)
        

    def show_employee_screen(self, user):
        """Ładuje widok dla Pracownika."""
        self._clear_window()

        #EmployeeView(self.root, user, self.logout)

    def logout(self):
        """Wylogowuje użytkownika i wraca do ekranu logowania."""

        self.show_login_screen()