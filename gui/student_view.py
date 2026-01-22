import tkinter as tk
from tkinter import messagebox
#tu będzie import z core dodający działania na danych

class StudentView:
    def __init__(self, root, user, logout):
        self.root = root
        
        self.setup_ui()

    def setup_ui(self):
        self.root.title("")
        self.root.geometry("800x600")
        self.root.resizable(False, False)
        
        

