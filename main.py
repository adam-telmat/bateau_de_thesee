from ship_classes import Part, Ship, RacingShip

def main():
    print("=== Le Paradoxe du Navire de Thésée ===")
    
    # Création du navire initial
    ship_name = input("Nom du navire: ")
    ship = Ship(ship_name)
    
    # Ajout des pièces initiales
    initial_parts = [
        Part("Mât", "Bois de pin"),
        Part("Coque", "Chêne"),
        Part("Voile", "Lin"),
        Part("Gouvernail", "Bois d'acajou")
    ]
    
    for part in initial_parts:
        ship.add_part(part)
    
    while True:
        print("\n=== Menu ===")
        print("1. Afficher l'état du navire")
        print("2. Remplacer une pièce")
        print("3. Modifier le matériau d'une pièce")
        print("4. Afficher l'historique")
        print("5. Quitter")
        
        choice = input("\nChoix: ")
        
        if choice == "1":
            ship.display_state()
            
        elif choice == "2":
            part_name = input("Nom de la pièce à remplacer: ")
            new_material = input("Nouveau matériau: ")
            try:
                new_part = Part(part_name, new_material)
                ship.replace_part(part_name, new_part)
                print(f"La pièce {part_name} a été remplacée.")
            except ValueError as e:
                print(f"Erreur: {e}")
                
        elif choice == "3":
            part_name = input("Nom de la pièce à modifier: ")
            new_material = input("Nouveau matériau: ")
            try:
                ship.change_part(part_name, new_material)
                print(f"Le matériau de {part_name} a été modifié.")
            except ValueError as e:
                print(f"Erreur: {e}")
                
        elif choice == "4":
            print("\nHistorique des modifications:")
            for entry in ship.get_history():
                print(entry)
                
        elif choice == "5":
            print("Au revoir!")
            break
            
        else:
            print("Option invalide")

if __name__ == "__main__":
    main() 