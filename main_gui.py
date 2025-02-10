import tkinter as tk
from ship_gui import ShipGUI
from ship_events import ShipEvent

def main():
    root = tk.Tk()
    app = ShipGUI(root)
    
    # Création du gestionnaire d'événements
    events = ShipEvent(app.ship)
    
    # Vérification périodique des événements aléatoires (toutes les 10 secondes)
    def check_events():
        events.check_random_event()
        app.display_state()
        root.after(10000, check_events)
    
    # Démarrage de la vérification des événements
    root.after(10000, check_events)
    
    root.mainloop()

if __name__ == "__main__":
    main() 