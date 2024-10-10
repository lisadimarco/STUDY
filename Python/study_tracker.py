import tkinter as tk
from tkinter import ttk
import json
import os
from datetime import datetime

class StudyTracker:
    def __init__(self, root):
        self.root = root
        self.root.title("Studio Gamificato")
        self.root.geometry("400x500")
        
        # Variabili
        self.time_studied = tk.IntVar(value=0)
        self.points = tk.IntVar(value=0)
        self.streak = tk.IntVar(value=0)
        
        # Carica i dati salvati
        self.load_data()
        
        # Stile
        style = ttk.Style()
        style.configure("TButton", padding=6, relief="flat", background="#2196F3")
        
        # Frame principale
        main_frame = ttk.Frame(root, padding="20")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Statistiche
        ttk.Label(main_frame, text="Studio Gamificato", font=('Helvetica', 16, 'bold')).grid(column=0, row=0, columnspan=2, pady=10)
        
        # Tempo studiato
        ttk.Label(main_frame, text="Tempo Studiato:", font=('Helvetica', 12)).grid(column=0, row=1, sticky=tk.W, pady=5)
        ttk.Label(main_frame, textvariable=self.time_studied, font=('Helvetica', 12, 'bold')).grid(column=1, row=1, sticky=tk.E)
        ttk.Label(main_frame, text="minuti", font=('Helvetica', 10)).grid(column=2, row=1, sticky=tk.W)
        
        # Punti
        ttk.Label(main_frame, text="Punti:", font=('Helvetica', 12)).grid(column=0, row=2, sticky=tk.W, pady=5)
        ttk.Label(main_frame, textvariable=self.points, font=('Helvetica', 12, 'bold')).grid(column=1, row=2, sticky=tk.E)
        
        # Serie
        ttk.Label(main_frame, text="Serie:", font=('Helvetica', 12)).grid(column=0, row=3, sticky=tk.W, pady=5)
        ttk.Label(main_frame, textvariable=self.streak, font=('Helvetica', 12, 'bold')).grid(column=1, row=3, sticky=tk.E)
        
        # Pulsante per aggiungere una sessione
        ttk.Button(main_frame, text="Completa 25 min di studio", command=self.add_session).grid(column=0, row=4, columnspan=3, pady=20)
        
        # Suggerimenti
        tips_frame = ttk.LabelFrame(main_frame, text="Suggerimenti", padding="10")
        tips_frame.grid(column=0, row=5, columnspan=3, sticky=(tk.W, tk.E), pady=10)
        
        tips = [
            "Usa il metodo Pomodoro: 25 min studio, 5 min pausa",
            "Spiega ad alta voce quello che hai studiato",
            "Crea esempi pratici per ogni concetto",
            "Disegna mappe mentali colorate"
        ]
        
        for i, tip in enumerate(tips):
            ttk.Label(tips_frame, text=f"• {tip}", wraplength=350).grid(column=0, row=i, sticky=tk.W, pady=2)
    
    def add_session(self):
        self.time_studied.set(self.time_studied.get() + 25)
        self.points.set(self.points.get() + 10)
        self.streak.set(self.streak.get() + 1)
        self.save_data()
    
    def save_data(self):
        data = {
            'time_studied': self.time_studied.get(),
            'points': self.points.get(),
            'streak': self.streak.get(),
            'last_session': datetime.now().isoformat()
        }
        with open('study_data.json', 'w') as f:
            json.dump(data, f)
    
    def load_data(self):
        try:
            with open('study_data.json', 'r') as f:
                data = json.load(f)
                self.time_studied.set(data.get('time_studied', 0))
                self.points.set(data.get('points', 0))
                self.streak.set(data.get('streak', 0))
        except FileNotFoundError:
            pass

if __name__ == "__main__":
    root = tk.Tk()
    app = StudyTracker(root)
    root.mainloop()
