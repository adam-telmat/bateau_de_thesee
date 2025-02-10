import tkinter as tk
from tkinter import ttk, messagebox
from ship_classes import Ship, Part

class ShipGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Navire de Thésée")
        self.ship = Ship("Thésée")
        
        # Initialisation des pièces par défaut
        self.init_default_parts()
        self.setup_gui()
        
    def init_default_parts(self):
        initial_parts = [
            Part("Mât", "Bois de pin"),
            Part("Coque", "Chêne"),
            Part("Voile", "Lin"),
            Part("Gouvernail", "Bois d'acajou")
        ]
        for part in initial_parts:
            self.ship.add_part(part)
        
    def setup_gui(self):
        # Frame principale
        self.main_frame = ttk.Frame(self.root, padding="10")
        self.main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Zone d'état du navire
        self.state_text = tk.Text(self.main_frame, height=10, width=50)
        self.state_text.grid(row=0, column=0, columnspan=2, pady=5)
        
        # Boutons
        ttk.Button(self.main_frame, text="Afficher état", 
                  command=self.display_state).grid(row=1, column=0, pady=5)
        ttk.Button(self.main_frame, text="Remplacer pièce", 
                  command=self.replace_part_dialog).grid(row=1, column=1, pady=5)
        ttk.Button(self.main_frame, text="Modifier matériau", 
                  command=self.change_material_dialog).grid(row=2, column=0, pady=5)
        ttk.Button(self.main_frame, text="Historique", 
                  command=self.show_history).grid(row=2, column=1, pady=5)

    def display_state(self):
        self.state_text.delete(1.0, tk.END)
        self.state_text.insert(tk.END, f"État du navire {self.ship.name}:\n\n")
        for part in self.ship._Ship__parts.values():
            self.state_text.insert(tk.END, f"- {part}\n")

    def replace_part_dialog(self):
        dialog = tk.Toplevel(self.root)
        dialog.title("Remplacer une pièce")
        
        # Liste des pièces existantes
        ttk.Label(dialog, text="Pièce à remplacer:").grid(row=0, column=0, pady=5)
        parts_list = ttk.Combobox(dialog, values=[part.name for part in self.ship._Ship__parts.values()])
        parts_list.grid(row=0, column=1, pady=5)
        
        # Liste des matériaux courants
        ttk.Label(dialog, text="Nouveau matériau:").grid(row=1, column=0, pady=5)
        materials = ["Bois de pin", "Chêne", "Acajou", "Lin", "Fer", "Acier", "Bronze"]
        new_material = ttk.Combobox(dialog, values=materials)
        new_material.grid(row=1, column=1, pady=5)
        
        def confirm():
            if not parts_list.get():
                messagebox.showerror("Erreur", "Veuillez sélectionner une pièce")
                return
            if not new_material.get():
                messagebox.showerror("Erreur", "Veuillez sélectionner ou saisir un matériau")
                return
            
            try:
                new_part = Part(parts_list.get(), new_material.get())
                self.ship.replace_part(parts_list.get(), new_part)
                self.display_state()
                dialog.destroy()
            except ValueError as e:
                messagebox.showerror("Erreur", str(e))
        
        ttk.Button(dialog, text="Confirmer", command=confirm).grid(row=2, column=0, columnspan=2, pady=10)

    def change_material_dialog(self):
        dialog = tk.Toplevel(self.root)
        dialog.title("Modifier le matériau")
        
        # Liste des pièces existantes
        ttk.Label(dialog, text="Pièce à modifier:").grid(row=0, column=0, pady=5)
        parts_list = ttk.Combobox(dialog, values=[part.name for part in self.ship._Ship__parts.values()])
        parts_list.grid(row=0, column=1, pady=5)
        
        # Liste des matériaux courants
        ttk.Label(dialog, text="Nouveau matériau:").grid(row=1, column=0, pady=5)
        materials = ["Bois de pin", "Chêne", "Acajou", "Lin", "Fer", "Acier", "Bronze"]
        new_material = ttk.Combobox(dialog, values=materials)
        new_material.grid(row=1, column=1, pady=5)
        
        def confirm():
            if not parts_list.get():
                messagebox.showerror("Erreur", "Veuillez sélectionner une pièce")
                return
            if not new_material.get():
                messagebox.showerror("Erreur", "Veuillez sélectionner ou saisir un matériau")
                return
            
            try:
                self.ship.change_part(parts_list.get(), new_material.get())
                self.display_state()
                dialog.destroy()
            except ValueError as e:
                messagebox.showerror("Erreur", str(e))
        
        ttk.Button(dialog, text="Confirmer", command=confirm).grid(row=2, column=0, columnspan=2, pady=10)

    def show_history(self):
        history_window = tk.Toplevel(self.root)
        history_window.title("Historique des modifications")
        
        history_text = tk.Text(history_window, height=20, width=60)
        history_text.pack(padx=10, pady=10)
        
        for entry in self.ship.get_history():
            history_text.insert(tk.END, f"{entry}\n") 