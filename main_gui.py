import tkinter as tk
from ship_gui import ShipGUI

def main():
    try:
        root = tk.Tk()
        app = ShipGUI(root)
        root.mainloop()
    except Exception as e:
        print(f"Erreur lors du lancement de l'interface graphique: {e}")
        print("Essayez de lancer la version console avec main.py")

if __name__ == "__main__":
    main() 