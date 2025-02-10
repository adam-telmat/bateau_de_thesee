from ship_classes import Part, Ship, RacingShip

def main():
    try:
        print("=== Le Paradoxe du Navire de Thésée ===")
        
        # Création du navire initial
        while True:
            ship_name = input("Nom du navire: ").strip()
            if ship_name:  # Vérifie que le nom n'est pas vide
                break
            print("Erreur: Le nom du navire ne peut pas être vide")
            
        ship = Ship(ship_name)
        
        # Ajout des pièces initiales
        try:
            initial_parts = [
                Part("Mât", "Bois de pin"),
                Part("Coque", "Chêne"),
                Part("Voile", "Lin"),
                Part("Gouvernail", "Bois d'acajou")
            ]
            
            for part in initial_parts:
                ship.add_part(part)
        except Exception as e:
            print(f"Erreur lors de l'initialisation des pièces: {e}")
            return
        
        while True:
            try:
                print("\n=== Menu ===")
                print("1. Afficher l'état du navire")
                print("2. Remplacer une pièce")
                print("3. Modifier le matériau d'une pièce")
                print("4. Afficher l'historique")
                print("5. Quitter")
                
                choice = input("\nChoix: ").strip()
                
                if choice == "1":
                    ship.display_state()
                    
                elif choice == "2":
                    part_name = input("Nom de la pièce à remplacer: ").strip()
                    if not part_name:
                        print("Erreur: Le nom de la pièce ne peut pas être vide")
                        continue
                        
                    new_material = input("Nouveau matériau: ").strip()
                    if not new_material:
                        print("Erreur: Le matériau ne peut pas être vide")
                        continue
                        
                    try:
                        new_part = Part(part_name, new_material)
                        ship.replace_part(part_name, new_part)
                        print(f"La pièce {part_name} a été remplacée.")
                    except ValueError as e:
                        print(f"Erreur: {e}")
                    
                elif choice == "3":
                    part_name = input("Nom de la pièce à modifier: ").strip()
                    if not part_name:
                        print("Erreur: Le nom de la pièce ne peut pas être vide")
                        continue
                        
                    new_material = input("Nouveau matériau: ").strip()
                    if not new_material:
                        print("Erreur: Le matériau ne peut pas être vide")
                        continue
                        
                    try:
                        ship.change_part(part_name, new_material)
                        print(f"Le matériau de {part_name} a été modifié.")
                    except ValueError as e:
                        print(f"Erreur: {e}")
                    
                elif choice == "4":
                    print("\nHistorique des modifications:")
                    history = ship.get_history()
                    if not history:
                        print("Aucune modification enregistrée")
                    else:
                        for entry in history:
                            print(entry)
                    
                elif choice == "5":
                    print("Au revoir!")
                    break
                    
                else:
                    print("Option invalide. Veuillez choisir entre 1 et 5.")
                    
            except KeyboardInterrupt:
                print("\nFermeture du programme...")
                break
            except Exception as e:
                print(f"Une erreur inattendue est survenue: {e}")
                print("Le programme continue...")
                
    except Exception as e:
        print(f"Erreur critique: {e}")
        print("Le programme doit s'arrêter.")

if __name__ == "__main__":
    main() 